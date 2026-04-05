class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def midpoint(self, other):
        return Point((self.x + other.x)/2, (self.y + other.y)/2)

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def __str__(self):
        return f"({self.x}, {self.y})"

class Circle:
    def __init__(self, centre=None, radius=1):
        if centre is None:
            self.centre = Point(0, 0)
        else:
            self.centre = centre
        
        self.radius = int(radius)

    def __str__(self):
        return f"Centre: {self.centre}\nRadius: {self.radius}"
    def __add__(self,other):
        new_centre = self.centre.midpoint(other.centre)
        new_radius = self.radius + other.radius
        return Circle(new_centre, new_radius)