import random as rnd
import model as model
import helper as hlp
import threading as threading


def IsCrit(critchance):
    return rnd.randrange(1, 100, 1) < critchance


def attack(attacker, deffender):
    dmg = attacker.AttackStrength
    if IsCrit(attacker.CritChance):
        dmg *= attacker.CritFactor
    dmg -= deffender.DefencePoints
    if dmg > 0:
        deffender.HealthPoints -= dmg

def getAverageRating(pool):
    average = 0.0
    for c in pool:
        average += float(c.Rating) / len(pool)
    return average


def battle(char1, char2):
    """
    :type char2: model.CharStats
    :type char1: model.CharStats
    """
    battleIsRunning = True
    timer = 0
    winner = None
    regTimer = 0.0
    char1AttackTimeStamp = char1.AttackSpeed
    char2AttackTimeStamp = char2.AttackSpeed
    char1Alive = True
    char2Alive = True
    while battleIsRunning and timer < 200:
        # char1 attack
        if timer > char1AttackTimeStamp:
            attack(char1, char2)
            char1AttackTimeStamp = timer + char1.AttackSpeed
        # char2 attack
        if timer > char2AttackTimeStamp:
            attack(char2, char1)
            char2AttackTimeStamp = timer + char2.AttackSpeed
        # char1 death
        if char1.HealthPoints < 0:
            char1Alive = False
            battleIsRunning = False
        # char1 death
        if char2.HealthPoints < 0:
            char2Alive = False
            battleIsRunning = False
        # health regen
        if timer > regTimer:
            regTimer = timer + 0.1
            # char1 regen
            char1.HealthPoints = hlp.clamp(char1.HealthRegenPerSecond / 10 + char1.HealthPoints, 0,
                                           char1.MaxHealthPoints)
            # char2 regen
            char2.HealthPoints = hlp.clamp(char2.HealthRegenPerSecond / 10 + char2.HealthPoints, 0,
                                           char2.MaxHealthPoints)
        timer += 0.1

    if char1Alive and not char2Alive:
        winner = char1

    if char2Alive and not char1Alive:
        winner = char2
    char1.HealthPoints = char1.MaxHealthPoints
    char2.HealthPoints = char2.MaxHealthPoints
    return winner

class battleThread(threading.Thread):
    def __init__(self, char1, char2, rounds):
        threading.Thread.__init__(self)
        self.char1 = char1
        self.char2 = char2
        self.rounds = rounds
    def run(self):
        for i in range(0, self.rounds):
            winner = battle(self.char1.Stats, self.char2.Stats)
            if winner is self.char1.Stats:
                self.char1.Lock.acquire()
                self.char1.Rating += 1
                self.char1.Lock.release()
                self.char2.Lock.acquire()
                self.char2.Rating -= 1
                self.char2.Lock.release()
            elif winner is self.char2.Stats:
                self.char1.Lock.acquire()
                self.char1.Rating -= 1
                self.char1.Lock.release()
                self.char2.Lock.acquire()
                self.char2.Rating += 1
                self.char2.Lock.release()



