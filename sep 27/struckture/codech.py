class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
p1 = Point(1,2)
print(p1)
print(repr(p1))
    