import generateChar as genChar
import model as model
from numpy.random import choice
import helper as hlp

powerLevel = 100
populationMax = 1000
populationMin = 500
iterations = 1000
roundsPerMatch = 50

population = []



def rate(pool):
    print "rate population"
    pb = hlp.ProgressBar(len(pool))
    for i in range(0, len(pool)):
        pool[i].rateAgainst(pool[(i+1)%(len(pool)-1)], roundsPerMatch/2)
        pb.progress(i)
    print "-Done"

def decimate(pool):
    """

    :type pool: list
    """
    print "decimate population"
    for c in pool:
        if c.Rating <= 0:
            pool.remove(c)
        if len(pool) < populationMin:
            break

    while len(pool) > populationMax:
        rate(pool)
        decimate(pool)
    print "##########"

def populate(pool):
    return


#initialPopulation
print "create first generation"
pb = hlp.ProgressBar(populationMax)
for i in range(1, populationMax):
    population.append(model.Character(genChar.generateRandom(powerLevel), powerLevel/2))
    pb.progress(i)
print "-Done"
#initialRating
rate(population)

#print ratings
# for c in population:
#     print c.Rating

