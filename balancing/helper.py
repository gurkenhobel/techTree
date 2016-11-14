import sys


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

class ProgressBar:
    def __init__(self, length):
        self.Length = length
        print ""
        self.CurrentState = 0
    def progress(self, value):
        if (value - self.CurrentState * (self.Length/10)) > self.Length/10:
            self.CurrentState += 1
            sys.stdout.write("#")