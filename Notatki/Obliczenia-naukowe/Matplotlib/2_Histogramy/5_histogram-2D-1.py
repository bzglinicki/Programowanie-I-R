# Programowanie I R
# Pakiet matplotlib
# Histogramy dwuwymiarowe - przykład 1.

# Dokumentacja:
#    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

import matplotlib.pyplot as plt

# Wykorzystamy ten pakiet do wygenerowania losowych danych.
import numpy as np

mean = [1, 3]
cov = [[1, 2], [1, 5]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T

# Rysujemy histogram dwuwymiarowy.
plt.hist2d(x, y, bins = 50, cmap = "Reds")
plt.colorbar().set_label("Zliczenia")

# Nadajemy wykresowi tytuł.
plt.title("Histogram 2D")

# Wyświetlamy wykres.
plt.show()