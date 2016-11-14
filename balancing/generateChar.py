from model import CharStats

import random as rnd

atkSpdFactor = 1
atkFactor = 1
critFactor = 1
deffFactor = 1
hpFactor = 1
regFactor = 1

baseStats = CharStats(1, 1, 5, 2, 0.5, 10, 0.1, 10)


def generateRandom(budget):
    char = baseStats.clone()
    rnd.seed()
    for i in range(1, budget):
        attr = rnd.randrange(1, 6, 1)
        if attr == 1:
            char.AttackSpeed -= atkSpdFactor
        elif attr == 2:
            char.AttackStrength += atkFactor
        elif attr == 3:
            char.CritChance += critFactor
        elif attr == 4:
            char.DefencePoints += deffFactor
        elif attr == 5:
            char.HealthPoints += hpFactor
            char.MaxHealthPoints += hpFactor
        elif attr == 6:
            char.HealthRegenPerSecond += regFactor
    return char

def mate(parent1, parent2):
    return  #CharStats

def mutate(char):
    return #CharStats

def clone(char):
    return char
