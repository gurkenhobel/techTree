import generateChar as genChar
import model as model
import helper as hlp

powerLevel = 100
populationMax = 500
populationMin = 100
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

def decimate(pool):
    """

    :type pool: list
    """
    print "decimate population"
    pb = hlp.ProgressBar(len(pool))
    for c in pool:
        if c.Rating <= 0:
            pool.remove(c)
            pb.progress(len(pool))
        if len(pool) < populationMin:
            break

    while len(pool) > populationMax:
        rate(pool)
        decimate(pool)

def populate(pool):
    return


#initialPopulation
print "create first generation"
pb = hlp.ProgressBar(populationMax -1)
for i in range(0, populationMax):
    population.append(model.Character(genChar.generateRandom(powerLevel), powerLevel/2))
    pb.progress(i)
pb.done()
#initialRating
rate(population)



