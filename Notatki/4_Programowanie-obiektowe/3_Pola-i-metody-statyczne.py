# Programowanie I R
# Programowanie obiektowe: pola i metody statyczne

class StaticDog:

    tricks = []   # Lista wspólna dla wszystkich instancji klasy.

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = StaticDog('Fido')
e = StaticDog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)   # ['roll over', 'play dead']
print(e.tricks)   # ['roll over', 'play dead']
print()

# **********************************************************************************

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []   # Każda z instancji klasy będzie posiadała niezależną listę.

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)   # ['roll over']
print(e.tricks)   # ['play dead']
print()

# **********************************************************************************

class Warehouse:
        purpose = 'storage'
        region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)   # storage west

w2 = Warehouse()
w2.region = 'east'
print(w1.purpose, w1.region)   # storage west
print(w2.purpose, w2.region)   # storage east

Warehouse.region = "south"
print(w1.purpose, w1.region)   # storage south
print(w2.purpose, w2.region)   # storage east

w2.__class__.region = "north"
print(w1.purpose, w1.region)   # storage south
print(w2.purpose, w2.region)   # storage east
print(w2.__class__.region)