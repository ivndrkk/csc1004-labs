from math import sqrt

class Point:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)
    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    def __str__(self):
        return f'({str(self.x)}, {str(self.y)})'