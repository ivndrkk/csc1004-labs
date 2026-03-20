import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"
