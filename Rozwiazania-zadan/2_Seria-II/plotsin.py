# Programowanie I R
# Zadania - seria 2.
# Zadanie 1.

import math
import matplotlib.pyplot as plt


#***********************************************************************************
# Funkcja frange
#***********************************************************************************

def frange(a, b, d = 1.0):
   res = []

   while True:
      x = float(a + len(res) * d)

      if d > 0 and x >= b:
         break
      elif d < 0 and x <= b:
         break
      
      res.append(x)
   
   return res

""" KOMENTARZ
Ta wersja funkcji frange nie jest idealna. Niektóre wartości na zwróconej przez tę
funkcję liście mogą się nieznacznie różnić od oczekiwanych ze względu na ograniczoną
precyzję liczb zmiennoprzecinkowych. Problem ten można rozwiązać, spowoduje to jednak,
że kod stanie się bardziej skomplikowany, tymczasem ta wersja funkcji wystarcza dla
naszych celów. Możliwe jest także przygotowanie szybszej wersji funkcji frange, ona
również będzie jednak bardziej skomplikowana.
"""


#***********************************************************************************
# Funkcja plotf
#***********************************************************************************

def plotf(f, a, b, d):
   x = frange(a, b, d)
   y = []

   for x0 in x:
      y.append(f(x0))
   
   plt.plot(x, y)

   plt.xlabel("$x$")
   plt.ylabel("$y$")
   plt.title("$y = f(x)$")
   
   plt.show()


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

# Pomocnicza funkcja f - zwraca wartości wykreślanej funkcji
def f(x):
   return x * math.sin(x) - x**2

print("Wykres funkcji f(x) = x sin x - x^2 w przedziale [a, b[ z krokiem d.")
a = float(input("\ta = ".expandtabs(3)))
b = float(input("\tb = ".expandtabs(3)))
d = float(input("\td = ".expandtabs(3)))

plotf(f, a, b, d)