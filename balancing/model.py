import fight as fight
import random as rnd
import generateChar as genChar
import threading as threading

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


    def rateAgainst(self, enemy, rounds, battleThread):
        """

        :type rounds: int
        :type enemy: Character
        """
        battleThread.char1 = self
        battleThread.char2 = enemy
        fight.battleThread(self, enemy, rounds)
        battleThread.start()
        return battleThread




