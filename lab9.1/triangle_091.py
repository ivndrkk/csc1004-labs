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

class Triangle:
    def __init__(self, a=Point(), b=Point(), c=Point()):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a.distance(self.b) + self.b.distance(self.c) + self.c.distance(self.a)
    def right_angle_triangle(self):
        return (self.a.distance(self.b)**2 + self.b.distance(self.c)**2 == self.c.distance(self.a)**2 or
                self.b.distance(self.c)**2 + self.c.distance(self.a)**2 == self.a.distance(self.b)**2 or
                self.c.distance(self.a)**2 + self.a.distance(self.b)**2 == self.b.distance(self.c)**2)