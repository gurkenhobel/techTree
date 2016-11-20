import fight as fight
import random as rnd
import generateChar as genChar


class CharStats:
    def __init__(self, atkSpd, atk, crit, critStr, deff, hp, maxHp, reg):
        self.AttackSpeed = atkSpd
        self.AttackStrength = atk
        self.CritChance = crit
        self.CritFactor = critStr
        self.DefencePoints = deff
        self.HealthPoints = hp
        self.MaxHealthPoints = maxHp
        self.HealthRegenPerSecond = reg

    def clone(self):
        return CharStats(self.AttackSpeed, self.AttackStrength, self.CritChance, self.CritFactor, self.DefencePoints,
                         self.HealthPoints, self.MaxHealthPoints, self.HealthRegenPerSecond)


class Character:
    def __init__(self, stats, rating):
        self.Stats = stats
        self.Rating = rating

    def rateAgainst(self, enemy, rounds):
        """

        :type rounds: int
        :type enemy: Character
        """

        for i in range(0, rounds - 1):
            winner = fight.battle(self.Stats, enemy.Stats)
            if winner is self.Stats:
                self.Rating += 1
                enemy.Rating -= 1
            elif winner is enemy.Stats:
                enemy.Rating += 1
                self.Rating -= 1
            if self.Rating > 100:
                self.Rating = 100
            if enemy.Rating > 100:
                enemy.Rating = 100




