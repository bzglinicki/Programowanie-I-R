# Programowanie I R
# Pakiet matplotlib
# Histogramy - przykład 3.

# Dokumentacja:
#    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

import matplotlib.pyplot as plt

# Wykorzystamy ten pakiet do wygenerowania losowych danych.
import numpy as np

# Generujemy trzy losowe tablice danych, opierając się na rozkładzie normalnym.
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

# Tworzymy słownik zawierający dodatkowe argumenty wywołania funkcji hist,
# by móc łatwo użyć ich wielokrotnie.
kwargs = dict(histtype = "stepfilled", alpha = 0.3, bins = 40)

# Rysujemy trzy histogramy
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)

# Podpisujemy osie.
plt.xlabel("x")
plt.ylabel("N")

# Nadajemy wykresowi tytuł.
plt.title("Rozkłady normalne")

# Wyświetlamy wykres.
plt.show()