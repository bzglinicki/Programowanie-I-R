# Programowanie I R
# Programowanie obiektowe: metody specjalne

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):   # ADDition - dodawanie
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __lt__(self, other):   # Less Then - mniejszy niż
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag


p1 = Point(1, 3)
p2 = Point(2, 5)

print(p1)
print(p2)
print(p1 + p2)

print(p1 < p2)
print(p1 > p2)