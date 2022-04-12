# Programowanie I R
# Programowanie obiektowe: iteratory

mytuple = ("żółw", "mysz", "chomik")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit)) - StopIteration, nie zadziała
print()

print("Pętla for:")
for x in mytuple:
  print(x)

print("********************************************")

# **********************************************************************************

mystr = "banan"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit)) - StopIteration, nie zadziała
print()

print("Pętla for:")
for x in mystr:
  print(x)

print("********************************************")

# Własne iteratory *****************************************************************

class NaturalNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

print("NaturalNumbers iterator:")
numbers = NaturalNumbers()
myiter = iter(numbers)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# Można tak w nieskończoność...
# Pętla for byłaby nieskończona!
print()

class Fifteen:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 15:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

print("NaturalNumbers iterator:")
numbers = Fifteen()

for x in numbers:
  print(x)

print()

class PowTwo:

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

print("Potęgi dwójki:")
numbers = PowTwo(5)
for i in numbers:
  print(i)