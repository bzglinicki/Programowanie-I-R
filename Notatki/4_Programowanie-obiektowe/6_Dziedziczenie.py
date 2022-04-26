# Programowanie I R
# Programowanie obiektowe: dziedziczenie

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class SimpleStudent(Person):
    pass

x = SimpleStudent("James", "Sullivan")
x.printname()
print()

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    #Person.__init__(self, fname, lname) - gorzej, wymaga podania nazwy klasy bazowej
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Wazowski", 2021)
x.printname()
x.welcome()

print()
print("********************************************************")
print()

class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

print()
print("********************************************************")
print()

# Polimorfizm **********************************************************************

class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")

class Dolphin:

    def fly(self):
        print("Dolphin can't fly")
    
    def swim(self):
        print("Dolphin can swim")

def flying_test(animal):
    animal.fly()

blu = Parrot()
rick = Dolphin()

flying_test(blu)
flying_test(rick)

print()
print("********************************************************")
print()

# Enkapsulacja *********************************************************************

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

print()
print("********************************************************")
print()

# **********************************************************************************

class Figure:
    def __init__(self, color):
        self.__color = color
    
    def getColor(self):
        return self.__color

class Circle(Figure):
    def __init__(self, color, r):
        super().__init__(color)
        self.__r = r

    def getRadius(self):
        return self.__r
    
    def getArea(self):
        import math
        return math.pi * self.__r * self.__r

class Rectangle(Figure):
    def __init__(self, color, a, b):
        super().__init__(color)
        self.__a = a
        self.__b = b
    
    def getFirstEdge(self):
        return self.__a

    def getSecondEdge(self):
        return self.__b
    
    def getArea(self):
        return self.__a * self.__b


c = Circle("red", 1.3)
r = Rectangle("green", 2.5, 1.8)

print(f"Okrąg:\n   promień: {c.getRadius()}\n   pole: {c.getArea()}")
print(f"Prostokąt:\n   pierwszy bok: {r.getFirstEdge()}\n   drugi bok: {r.getSecondEdge()}\n   pole: {r.getArea()}")
print()

print(isinstance(c, Figure))
print(isinstance(c, Circle))
print(isinstance(c, Rectangle))
print()

print(isinstance(r, Figure))
print(isinstance(r, Circle))
print(isinstance(r, Rectangle))
print()

print(issubclass(Circle, Figure))
print(issubclass(Figure, Circle))

print(issubclass(Rectangle, Figure))
print(issubclass(Figure, Rectangle))

print(issubclass(Circle, Rectangle))
print(issubclass(Rectangle, Circle))

print()

print(isinstance(c, object))
print(isinstance(r, object))

print(issubclass(Circle, object))
print(issubclass(Rectangle, object))
print(issubclass(Figure, object))

print(issubclass(int, object))