class Score:
    
    def __init__(self,goals=0,points=0):
        self.goals = goals
        self.points = points
        
    def __str__(self):
        return f"{self.goals} goal(s) and {self.points} point(s)"
    
    def total_points(self):
        return self.goals * 3 + self.points
    
    def __eq__(self,other):
        return self.total_points() == other.total_points()
    def __gt__(self,other):
        return self.total_points() > other.total_points()
    def __lt__(self,other):
        return self.total_points() < other.total_points()
    def __le__(self,other):
        return self.total_points() <= other.total_points()
    def __ge__(self,other):
        return self.total_points() >= other.total_points()
    def __ne__(self,other):
        return self.total_points() != other.total_points()
    
    def __add__(self,other):
        return Score(self.goals + other.goals, self.points + other.points)
    def __iadd__(self,other):
        self.goals += other.goals
        self.points += other.points
        return self