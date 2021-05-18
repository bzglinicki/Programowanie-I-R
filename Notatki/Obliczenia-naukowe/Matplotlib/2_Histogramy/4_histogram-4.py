# Programowanie I R
# Pakiet matplotlib
# Histogramy - przykład 4. (zaawansowany)

# Przykład pochodzi ze strony
#    https://matplotlib.org/stable/gallery/statistics/hist.html

# Dokumentacja:
#    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

import matplotlib
import matplotlib.pyplot as plt

# Wykorzystamy ten pakiet do wygenerowania losowych danych.
import numpy as np

N_points = 100000
n_bins = 20

# Generujemy rozkład normalny.
x = np.random.randn(N_points)

# Dzielimy płótno poziomo na dwie części, by móc narysować dwa wykresy.
fig, axs = plt.subplots(1, 2, tight_layout = True)

# Funkcja hist() zwraca krotkę złożoną z trzech wielkości:
#    N -       tablica wartości kolejnych słupków histogramu;
#    bins -    tablica położeń lewych brzegów kolejnych słupków
#              oraz prawego brzegu ostatniego słupka;
#    patches - lista zawierająca kolejne słupki.
N, bins, patches = axs[0].hist(x, bins = n_bins)

# Kolor słupka będzie zależał od jego wysokości.
# Musimy zormalizować dane do przedziału [0, 1].
fracs = N / N.max()
norm = matplotlib.colors.Normalize(fracs.min(), fracs.max())

# Za pomocą pętli for ustalamy kolor każdego ze słupków na pierwszym wykresie niezależnie.
# Funkcja zip() zwraca krotkę zbudowaną z kolejnych elementów swoich argumentów.
for thisfrac, thispatch in zip(fracs, patches):
   color = plt.cm.viridis(norm(thisfrac))   # Opis funkcji w dokumentacji
   thispatch.set_facecolor(color)           # pakietu matplotlib.

# Normujemy drugi histogram.
axs[1].hist(x, bins = n_bins, density = True)

# Formatujemy pionową oś drugiego histogramu tak, by wyświetlała wartości procentowe.
axs[1].yaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(xmax = 1))

# Wyświetlamy wykresy.
plt.show()