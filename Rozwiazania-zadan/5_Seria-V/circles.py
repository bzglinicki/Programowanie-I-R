# Programowanie I R
# Zadania - seria 4.
# Zadanie 1.

import math
import sys


#***********************************************************************************
# Klasa Circle
#***********************************************************************************

class Circle:
   def __init__(self, x = 0., y = 0., r = 1.):
      self.x = x
      self.y = y
      self.r = r
            
   def circumference(self):
      return 2 * math.pi * self.r
    
   def intersection(self, c):
      # Odległość między środkami okręgów.
      d = math.sqrt((self.x - c.x)**2 + (self.y - c.y)**2)

      if (d == 0) and (self.r == c.r):   # Okręgi identyczne.
         return math.inf
      elif d > self.r + c.r:             # Okręgi rozłączne zewnętrznie.
         return 0
      elif d < abs(self.r - c.r):        # Okręgi rozłączne wewnętrznie.
         return 0
      elif d == self.r + c.r:            # Okręgi styczne zewnętrznie.
         return 1
      elif d == abs(self.r - c.r):       # Okręgi styczne wewnętrznie.
         return 1
      elif (abs(self.r - c.r) < d) and (d < self.r + c.r):   # Okręgi przecinające się.
         return 2


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

if len(sys.argv) != 7:
   print("Błąd! Niepoprawna liczba argumentów.")
   quit()

# Pierwszy okrąg.
c1 = Circle(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))

# Drugi okrąg.
c2 = Circle(float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]))

# Liczba punktów wspólnych.
n = c1.intersection(c2)
# Równoważnie: n = c2.intersection(c1)

print("Okręgi")
print(f"   C1 o środku w punkcie ({c1.x}, {c1.y}) i promieniu {c1.r}")
print("oraz")
print(f"   C2 o środku w punkcie ({c2.x}, {c2.y}) i promieniu {c2.r}")

if n == 0: print("nie mają punktów wspólnych.")
elif n == 1: print("mają jeden punkt wspólny.")
elif n == 2: print("mają dwa punkty wspólne.")
elif math.isinf(n): print("mają nieskończenie wiele punktów wspólnych.")
else: print("Błąd! Nie udało się określić liczby punktów wspólnych okręgów.")