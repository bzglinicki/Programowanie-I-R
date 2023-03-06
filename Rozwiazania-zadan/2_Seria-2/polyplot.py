# Programowanie I R
# Zadania - seria 2.
# Zadanie 3.

import datetime
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


#***********************************************************************************
# Funkcje pomocnicze
#***********************************************************************************

def f1(x):
   return 3 * (x - 1)

def f2(x):
   return 3 * (x - 1) * (x - 2)

def f3(x):
   return 3 * (x - 1) * (x - 2) * (x - 3)

def f4(x):
   return 3 * (x - 1) * (x - 2) * (x - 3) * (x - 4)

def f5(x):
   return 3 * (x - 1) * (x - 2) * (x - 3) * (x - 4) * (x - 5)


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

with PdfPages("polyplot.pdf") as pdf:
   functions = [f1, f2, f3, f4, f5]
   x = [k / 10 for k in range(10, 56)]

   for i in range(5):
      y = []
      for x0 in x:
         y.append(functions[i](x0))
      
      fig = plt.figure()
      plt.plot(x, y)
      plt.xlabel("$x$")
      plt.ylabel("$y$")
      plt.title(f"Wykres funkcji $y = f_{i + 1}(x)$")
      plt.grid()
      pdf.savefig(fig)
      plt.close()

   d = pdf.infodict()
   d["Title"] = "Wykresy pięciu wielomianów"
   d["Author"] = "Bartłomiej Zglinicki"
   d["Subject"] = "Programowanie I R"
   d["Keywords"] = "wykres funkcja wielomian"
   d["CreationDate"] = datetime.datetime.today()
   d["ModDate"] = datetime.datetime.today()