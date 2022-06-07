# Programowanie I R
#
# Równania różniczkowe
# Przykład: rozwiązywanie równania ruchu oscylatora harmonicznego
#           metodą Eulera

"""
Ruch oscylatora harmonicznego o częstości omega opisuje równanie
   x'' + omega^2 x = 0,
w którym szukana funkcja x = x(t). Równanie to należy do klasy
liniowych jednorodnych równań różniczkowych zwyczajnych drugiego rzędu.
Wprowadzając zmienną v = x' możemy zastąpić je równoważnym układem dwóch
równań pierwszego rzędu:
   x' = v,
   v' = - omega^2 x.
Właśnie ten układ równań różniczkowych zwyczajnych pierwszego rzędu
rozwiążemy numerycznie, posługując się metodą punktu środkowego.
Przyjmujemy warunki początkowe:
   x(0) = x0,
   v(0) = v0.

Znane jest analityczne rozwiązanie równania ruchu oscylatora harmonicznego.
Można je przedstawić w postaci
   x(t) = A sin(omega t) + B cos (omega t),
gdzie stałe A i B wyznaczone są przez warunku początkowe:
   A = v0 / omega,
   B = x0.
Porównamy otrzymane rozwiązanie numeryczne z rozwiązaniem analitycznym.
"""


import sys
import numpy as np
import matplotlib.pyplot as plt


#***********************************************************************************
# Funkcje pomocnicze
#***********************************************************************************

# Prawa strona równania x' = v *****************************************************
def Fx(v):
   return v

# Prawa strona równania v' = - omega^2 x *******************************************
def Fv(omega, x):
   return - (omega ** 2) * x

# Wynik analityczny - położenie oscylatora *****************************************
def SolveExact(omega, x0, v0, t):
   A = v0 / omega
   B = x0
   return A * np.sin(omega * t) + B * np.cos(omega * t)


#***********************************************************************************
# Funkcja SolveEuler: rozwiązywanie równania różniczkowego metodą punktu środkowego
#***********************************************************************************

# Argumenty:
#    x0 - położenie początkowe,
#    v0 - prędkość początkowa,
#    tmax - przedział czasu,
#    dt - krok czasowy.

def SolveMidpoint(omega, x0, v0, tmax, dt):
   # Zmienne x i v będą przechowywały, odpowiednio, położenie i prędkość oscylatora
   # w danej iteracji. Na początek przypisujemy im więc wartości początkowe.
   x, v  =  x0, v0
   
   # Tworzymy listy, które będą przechowywały wyniki obliczeń uzyskane w kolejnych
   # iteracjach. Kolejne elementy list będą sobie wzajemnie odpowiadały, np. res_x[3]
   # będzie położeniem oscylatora w chwili res_t[3], zaś np. res_v[5] - prędkością
   # oscylatora w chwili res_t[5]. Na listach umieszczamy od razu wartości początkowe.
   
   #    res_t - kolejne chwile, różniące się od siebie o dt
   res_t = [0]
   
   #    res_x - położenia oscylatora w kolejnych chwilach
   res_x = [x0]
   
   #    res_v - prędkości oscylatora w kolejnych chwilach
   res_v = [v0]
   
   # Dla zobraozwania dokładności metody numerycznej, którą stosujemy, obliczymy też
   # dokładne wartości położenia oscylatora w kolejnych chwilach, uzyskane na podstawie
   # rozwiązania analitycznego, oraz różnicę pomiędzy wartością dokładną a numeryczną.
   
   #    res_exact - położenia oscylatora w kolejnych chwilach - wynik analityczny
   res_exact = [x0]
   
   #    res_diff - różnica pomiędzy wynikiem analitycznym a numerycznym
   res_diff  = [0]

   # Główna pętla przeprowadzająca kolejne iteracje algorytmu
   for t in np.arange(dt, tmax, dt):
      # Obliczamy nowe wartości położenia i prędkości
      x_aux = x + dt * Fx(v) / 2.
      v_aux = v + dt * Fv(omega, x) / 2.
      
      xn = x + dt * Fx(v_aux)
      vn = v + dt * Fv(omega, x_aux)
      
      # Dopisujemy te wartości do list zawierających wyniki
      res_t += [t]
      res_x += [xn]
      res_v += [vn]
      
      # Obliczamy też wartość analityczną dla danej chwili oraz różnicę pomiędzy
      # wartościami analityczną i numeryczną oraz dopisujemy je do odpowiednich list.
      x_exact = SolveExact(omega, x0, v0, t)
      res_exact += [x_exact]
      res_diff  += [x_exact - x]
      
      # Przygotowujemy się do kolejnej iteracji, aktualizując zmienne x i v
      x, v = xn, vn
   
   # Po wykonaniu wszystkich iteracji zwracamy otrzymane wyniki
   return res_t, res_x, res_v, res_exact, res_diff


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

# Odczytujemy argumenty wywołania
omega = float(sys.argv[1])
x0 = float(sys.argv[2])
v0 = float(sys.argv[3])
tmax = float(sys.argv[4])
dt = float(sys.argv[5])

# Wołamy funkcję rozwiązującą równanie
res_t, res_x, res_v, res_exact, res_diff = SolveMidpoint(omega, x0, v0, tmax, dt)

# Rysyjemy wyniki
fig = plt.figure(constrained_layout = True)

fig.suptitle("Oscylator harmoniczny - metoda Eulera", fontsize = "xx-large")

subfigs = fig.subfigures(1, 2, wspace=0.07)

subfigs[1].suptitle("Diagram fazowy")

axs = subfigs[0].subplots(2)
axs[0].plot(res_t, res_x, 'r-', label = "Rozwiązanie numeryczne")
axs[0].plot(res_t, res_exact, 'b-', label = "Rozwiązanie analityczne")
axs[0].set_title("Rozwiązania: analityczne (czerwone) i numeryczne (niebieskie)")
axs[0].grid()

axs[1].plot(res_t, res_diff, 'g-')
axs[1].set_title("Różnica pomiędzy rozwiązaniem analitycznym a numerycznym")
axs[1].grid()

for ax in axs.flat:
    ax.set(xlabel = "t", ylabel = "x")

for ax in axs.flat:
    ax.label_outer()
    
axr = subfigs[1].subplots()
axr.plot(res_x, res_v)
axr.grid()
axr.set(xlabel = "x", ylabel = "v")

plt.show()