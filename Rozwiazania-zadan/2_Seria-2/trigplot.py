# Programowanie I R
# Zadania - seria 2.
# Zadanie 2.

import math
import matplotlib.pyplot as plt


#***********************************************************************************
# Funkcja gfrange
#***********************************************************************************

def gfrange(a, b, d = 1.0):
   n = 0

   while True:
      x = float(a + n * d)

      if d > 0 and x >= b:
         break
      elif d < 0 and x <= b:
         break
      
      yield x
      n += 1

""" KOMENTARZ
Ta wersja funkcji gfrange nie jest idealna. Niektóre ze zwracanych przez nią wartości
mogą się nieznacznie różnić od oczekiwanych ze względu na ograniczoną precyzję liczb
zmiennoprzecinkowych. Problem ten można rozwiązać, spowoduje to jednak, że kod stanie
się bardziej skomplikowany, tymczasem ta wersja funkcji wystarcza dla naszych celów.
"""


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

# Pomocnicza funkcja plot - przygotowuje dane i rysuje wykresy
def plot():
   # Przygotowanie danych

   x = list(gfrange(-0.5, 0.5, 0.01))
   y_sin = []
   y_tg = []

   for x0 in x:
      y_sin.append(math.sin(x0))
      y_tg.append(math.tan(x0))

   # Rysowanie wykresów

   plt.plot(x, x, label = "$y = x$")
   plt.plot(x, y_sin, label = r"$y = \sin x$")
   plt.plot(x, y_tg, label = r"$y = \mathrm{tg} x$")

   plt.xlabel("$x$")
   plt.ylabel("$y$")
   plt.title("Wykresy funkcji: liniowej, sinus i tangens")
   plt.legend()


# Wyświetlenie rysunku na ekranie

plot()
plt.show()

# Zapis rysunku do pliku

print("Czy zapisać rysunek do pliku? Jeśli tak, podaj format (png, jpg, svg lub pdf).")
format = input()

if format.lower() == "png":
   plot()
   plt.savefig("trigplot.png", dpi = 300, transparent = True)
   print("Rysunek został zapisany w pliku trigplot.png.")
elif format.lower() == "jpg":
   plot()
   plt.savefig("trigplot.jpg", dpi = 300)
   print("Rysunek został zapisany w pliku trigplot.jpg.")
elif format.lower() == "svg":
   plot()
   plt.savefig("trigplot.svg")
   print("Rysunek został zapisany w pliku trigplot.svg.")
elif format.lower() == "pdf":
   plot()
   plt.savefig("trigplot.pdf")
   print("Rysunek został zapisany w pliku trigplot.pdf.")
else:
   print("Rysunek nie został zapisany.")