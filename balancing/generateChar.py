from model import CharStats

import random as rnd

atkSpdFactor = 1
atkFactor = 1
critFactor = 1
critChanceFactor = 1
deffFactor = 1
hpFactor = 1
regFactor = 1

baseStats = CharStats(1, 1, 5, 2, 0.5, 10, 10, 0.1)


def generateRandom(budget):
    char = baseStats.clone()
    rnd.seed()
    for i in range(0, budget):
        attr = rnd.randrange(1, 7, 1)
        if attr == 1:
            char.AttackSpeed -= atkSpdFactor    #TODO: attackspeed < 0 ?
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


def mate(parent1, parent2):
    """

    :type budget: int
    :type parent2: CharStats
    :type parent1: CharStats
    """

    budget = parent1.AttackSpeed / atkSpdFactor + parent1.AttackStrength / atkFactor + parent1.CritChance / critChanceFactor + parent1.CritFactor /critFactor + parent1.DefencePoints /deffFactor + parent1.HealthPoints /hpFactor + parent1.HealthRegenPerSecond /regFactor
    print "1 -",budget - 29.6
    budget = parent2.AttackSpeed / atkSpdFactor + parent2.AttackStrength / atkFactor + parent2.CritChance / critChanceFactor + parent2.CritFactor / critFactor + parent2.DefencePoints / deffFactor + parent2.HealthPoints / hpFactor + parent2.HealthRegenPerSecond / regFactor
    print "2 -", budget -29.6

    attackSpeed = (parent1.AttackSpeed + parent2.AttackSpeed)/2
    attackStrength = (parent1.AttackStrength + parent2.AttackStrength)/2
    critChance = (parent1.CritChance + parent2.CritChance)/2
    crtFactor = (parent1.CritFactor + parent2.CritFactor)/2
    deffPoints = (parent1.DefencePoints + parent2.DefencePoints)/2
    healthPoints = (parent1.MaxHealthPoints + parent2.MaxHealthPoints)/2
    regen = (parent1.HealthRegenPerSecond + parent2.HealthRegenPerSecond)/2

    newChar = CharStats(attackSpeed, attackStrength,critChance,crtFactor,deffPoints,healthPoints,healthPoints,regen)

    budget = newChar.AttackSpeed / atkSpdFactor + newChar.AttackStrength / atkFactor + newChar.CritChance / critChanceFactor + newChar.CritFactor / critFactor + newChar.DefencePoints / deffFactor + newChar.HealthPoints / hpFactor + newChar.HealthRegenPerSecond / regFactor
    print budget

    return  newChar


def mutate(char):
    return  # CharStats


def clone(char):
    return char
