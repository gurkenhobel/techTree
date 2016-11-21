from model import CharStats

import random as rnd
import helper as hlp

atkSpdFactor = 0.05
atkFactor = 0.95
critFactor = 1
critChanceFactor = 1
deffFactor = 1
hpFactor = 1.5
regFactor = 1

baseStats = CharStats(1, 1, 5, 2, 0.5, 10, 10, 0.1)


def generateRandom(budget):
    char = baseStats.clone()
    rnd.seed()
    for i in range(0, budget):
        attr = rnd.randrange(1, 8, 1)
        if char.AttackSpeed <= 0.1 and attr == 1:
            attr = rnd.randrange(2, 8, 1)
        if attr == 1:
            char.AttackSpeed -= atkSpdFactor
            if char.AttackSpeed <= 0:
                char.AttackSpeed = 0.1
        elif attr == 2:
            char.AttackStrength += atkFactor
        elif attr == 3:
            char.CritChance += critChanceFactor
        elif attr == 4:
            char.DefencePoints += deffFactor
        elif attr == 5:
            char.HealthPoints += hpFactor
            char.MaxHealthPoints += hpFactor
        elif attr == 6:
            char.HealthRegenPerSecond += regFactor
        elif attr == 7:
            char.CritFactor += critFactor
        else:
            print "error!"
    return char


def mate(parent1, parent2, targetBudget):
    """

    :type budget: int
    :type parent2: CharStats
    :type parent1: CharStats
    """


    attackSpeed = (parent1.AttackSpeed + parent2.AttackSpeed)/2
    attackStrength = (parent1.AttackStrength + parent2.AttackStrength)/2
    critChance = (parent1.CritChance + parent2.CritChance)/2
    crtFactor = (parent1.CritFactor + parent2.CritFactor)/2
    deffPoints = (parent1.DefencePoints + parent2.DefencePoints)/2
    healthPoints = (parent1.MaxHealthPoints + parent2.MaxHealthPoints)/2
    regen = (parent1.HealthRegenPerSecond + parent2.HealthRegenPerSecond)/2

    newChar = CharStats(attackSpeed, attackStrength,critChance,crtFactor,deffPoints,healthPoints,healthPoints,regen)


    budget = (baseStats.AttackSpeed - newChar.AttackSpeed) / atkSpdFactor + newChar.AttackStrength / atkFactor + newChar.CritChance / critChanceFactor + newChar.CritFactor / critFactor + newChar.DefencePoints / deffFactor + newChar.HealthPoints / hpFactor + newChar.HealthRegenPerSecond / regFactor


    newChar.HealthPoints += targetBudget - (budget - 18.6)      #loss in the estimation between parents. adds to health because of reasons. 18.6 is the value of the basestats

    return  newChar


def mutate(char):
    return  # CharStats


def clone(char):
    return char
