import sys
import math as math


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

class ProgressBar:
    def __init__(self, length):
        self.Length = length
        sys.stdout.write("[")
        self.CurrentState = 0
    def progress(self, value):
        if (value - self.CurrentState * (self.Length/10)) > self.Length/10:
            state = int(10 - math.floor ((self.Length - value) / (self.Length / 10)))
            for i in range(0, state - self.CurrentState):
                sys.stdout.write("#")
            self.CurrentState = state
    def done(self):
        print "]-Done"


def printAllFields(instance):
    v = dict(instance.__dict__)

    for n in v.keys():
        print n, v[n]
