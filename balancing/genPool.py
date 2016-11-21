import generateChar as genChar
import model as model
import helper as hlp
import random as rnd
import fight as fight
import threading as trdng
import multiprocessing as mltpcssng

powerLevel = 100
populationMax = 50
populationMin = 40
iterations = 100
roundsPerMatch = 4

population = []

maxThreads = 4
if maxThreads > mltpcssng.cpu_count():
    maxThreads = mltpcssng.cpu_count()


def rate(pool):
    print "rate population"
    threadsIdle = maxThreads
    threadsActive = []
    pb = hlp.ProgressBar(len(pool) - 1)
    for i in range(0, len(pool)):
        for e in range(0, len(pool)):
            if e != i:
                thread = fight.battleThread(None,None,roundsPerMatch/2)
                threadsIdle -= 1
                pool[i].rateAgainst(pool[e], roundsPerMatch/2, thread)
                threadsActive.append(thread)
                while threadsIdle == 0:
                    for t in threadsActive:
                        if not t.isActive:
                            threadsActive.remove(t)
                            threadsIdle += 1

        pb.progress(i)
    for t in threadsActive:
        if t.isAlive():
            t.join()
    pb.done()

def killBelowRating(limit, pool):
    for c in pool:
        if(c.Rating < limit):
            pool.remove(c)
        if(len(pool) < populationMin):
            break

def decimate(pool):
    """

    :type pool: list
    """
    print "decimate population"
    for c in pool:
        #clean out negative ratings
        if c.Rating <= 0:
            pool.remove(c)
        if len(pool) < populationMin:
            break

    # random = rnd.randrange(0,0)
    # if random == 1:
    limit = fight.getAverageRating(pool)

    killBelowRating(limit, pool)

    for c in population:
        c.Rating = 50


    while len(pool) > populationMin:
        rate(pool)
        decimate(pool)

def populate(pool, i):
    print "create generation", i
    pb = hlp.ProgressBar(populationMax - 1)
    for i in range(0, populationMax):
        method = rnd.randrange(0,1)
        if  method == 0:
            pool.append(model.Character(genChar.generateRandom(powerLevel), 50))
            pb.progress(i)
        elif method == 1:
            p1 = pool[rnd.randrande(0, len(pool - 1))].Stats
            p2 = pool[rnd.randrande(0, len(pool - 1))].Stats
            pool.append(model.Character(genChar.mate(p1, p2, powerLevel)), 50)
    pb.done()
    return


#initialPopulation
print "create first generation"
pb = hlp.ProgressBar(populationMax -1)
for i in range(0, populationMax):
    population.append(model.Character(genChar.generateRandom(powerLevel), 50))
    pb.progress(i)
pb.done()
#initialRating
rate(population)
g = 1
for i in range(1, iterations):
    decimate(population)
    g += 1
    populate(population, g)
    rate(population)


best = population[0]
worst = population[0]

for i in range(1, len(population)):
    if population[i].Rating > best.Rating:
        best = population[i]
    if population[i].Rating < worst.Rating:
        worst = population[i]
print "final Generation"

print "best Rating:", best.Rating
print "Stats:\n"
hlp.printAllFields(best.Stats)

print "worst Rating:", worst.Rating
print "Stats:\n"
hlp.printAllFields(worst.Stats)


