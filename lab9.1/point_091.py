class Point:
    def __init__(self,x=0.0,y=0.0):
        self.x = float(x)
        self.y = float(y)
    def midpoint(self,other):
        return Point((self.x + other.x)/2, (self.y + other.y)/2)
    def distance(self,other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    def __str__(self):
        return f"({self.x}, {self.y})"
    
