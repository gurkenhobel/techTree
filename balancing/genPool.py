import generateChar as genChar
import model as model
import helper as hlp
import random as rnd
import fight as fight

powerLevel = 100
populationMax = 1000
populationMin = 500
iterations = 1000
roundsPerMatch = 50

population = []



def rate(pool):
    print "rate population"
    pb = hlp.ProgressBar(len(pool) - 1)
    for i in range(0, len(pool)):
        pool[i].rateAgainst(pool[(i+1)%(len(pool)-1)], roundsPerMatch/2)
        pb.progress(i)
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
        pool.append(model.Character(genChar.generateRandom(powerLevel), 50))
        pb.progress(i)
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
for i in range(0, iterations):
    decimate(population)
    g += 1
    populate(population, g)
    rate(population)






