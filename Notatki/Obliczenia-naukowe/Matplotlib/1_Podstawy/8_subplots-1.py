# Programowanie I R
# Pakiet matplotlib
# Wiele wykresów na jednym płótnie - przykład 1.

# Dokumentacja:
#    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

# Przydatne materiały
#    https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html

import math
import matplotlib
import matplotlib.pyplot as plt

# Określamy dyskretny zbiór argumentów i obliczamy wartości funkcji
x = [x * 0.1 for x in range(0, 70)]

y1 = []
for x0 in x:
    y1.append(math.sin(x0))

y2 = []
for x0 in x:
    y2.append(math.cos(x0))

# Funkcja subplots() dzieli płótno na części. W każdej z nich można narysować inny wykres.
# Pierwszy argument to liczba wierszy, a drugi - liczba kolumn podzielonego płótna.
# Funkcja subplots() zwraca krotkę złożoną z dwóch wielkości:
#    fig - całe płótno;
#    axs - tablica poszczególnych części płótna.
fig, axs = plt.subplots(2, 1)   # Równoważne plt.subplots(2)

# Tytuł płótna, wspólny dla wszystkich wykresów.
fig.suptitle("Dwa wykresy")

# W poszczególnych częściach płótna rysujemy wykresy.
axs[0].plot(x, y1)
axs[1].plot(x, y2)

# Wyświetlamy wykresy.
plt.show()