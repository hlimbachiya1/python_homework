import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

if __name__ == "__main__":
    p = Point(1, 2)
    q = Point(1, 2)
    print(p, q, p == q)
    print("Distance:", p.distance_to(Point(4, 6)))
    
    v1 = Vector(1, 0)
    v2 = Vector(0, 2)
    v3 = v1 + v2
    print(v1, v2, v3)