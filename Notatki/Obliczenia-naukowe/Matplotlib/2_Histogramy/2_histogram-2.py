# Programowanie I R
# Pakiet matplotlib
# Histogramy - przykład 2.

# Dokumentacja:
#    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

import matplotlib.pyplot as plt

# Dane do przedstawienia na histogramie. W naszym przykładzie
# narysujemy histogram wieku pewnej grupy osób.
data = [1, 1, 2, 3, 3, 5, 7, 8, 9, 10, 
     10, 11, 11, 13, 13, 15, 16, 17, 18, 18, 
     18, 19, 20, 21, 21, 23, 24, 24, 25, 25, 
     25, 25, 26, 26, 26, 27, 27, 27, 27, 27, 
     29, 30, 30, 31, 33, 34, 34, 34, 35, 36, 
     36, 37, 37, 38, 38, 39, 40, 41, 41, 42, 
     43, 44, 45, 45, 46, 47, 48, 48, 49, 50, 
     51, 52, 53, 54, 55, 55, 56, 57, 58, 60, 
     61, 63, 64, 65, 66, 68, 70, 71, 72, 74, 
     75, 77, 81, 83, 84, 87, 89, 90, 90, 91
     ]
  
# Zakres osi Ox.
r = (0, 100)

# Rozpiętość przedziałów.
bins = 10
  
# Rysujemy histogram.
plt.hist(data, bins, r,
      color = "#0504aa",         # Kolor wypełnienia słupków.
      edgecolor = "steelblue",   # Kolor obramowania słupków.
      histtype = "bar",          # Typ histogramu.
      rwidth = 0.9               # Stosunek szerokości słupka do szerokości przedziału.
)

# Rysujemy siatkę dla osi Oy. Parametr "alpha" określa przezroczystość.
plt.grid(axis = "y", alpha = 0.75)

# Podpisujemy osie.
plt.xlabel("Wiek")
plt.ylabel("Liczebność")

# Nadajemy wykresowi tytuł.
plt.title("Rozkład wieku")

# Wyświetlamy wykres.
plt.show()