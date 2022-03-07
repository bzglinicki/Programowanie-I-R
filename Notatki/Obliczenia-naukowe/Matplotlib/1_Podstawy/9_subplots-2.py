# Programowanie I R
# Pakiet matplotlib
# Wiele wykresów na jednym płótnie - przykład 2.

# Przykład opracowany na podstawie kodu ze strony
#    https://www.geeksforgeeks.org/graph-plotting-python-set-2/

# Dokumentacja:
#    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

# Przydatne materiały
#    https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html

import math
import matplotlib
import matplotlib.pyplot as plt

# Metoda wyznaczająca punkty niezbędne
# do narysowania każdego z wykresów.
def create_plot(n): 
    x = [x * 0.1 for x in range(-100, 100)]
    y = []

    for x0 in x:
        y.append(x0**n)

    return (x, y)

# Funkcja subplots() dzieli płótno na części. W każdej z nich można narysować inny wykres.
# Pierwszy argument to liczba wierszy, a drugi - liczba kolumn podzielonego płótna.
# Argument "tight_layout = True" zapewnia dopasowanie odstępów między wykresami.
# Funkcja subplots() zwraca krotkę złożoną z dwóch wielkości:
#    fig - całe płótno;
#    axs - tablica poszczególnych części płótna.
fig, axs = plt.subplots(2, 2, tight_layout = True)

# Tytuł płótna, wspólny dla wszystkich wykresów.
fig.suptitle("Cztery jednomiany")

# W poszczególnych częściach płótna rysujemy wykresy.
x, y = create_plot(1)
axs[0, 0].plot(x, y, color = "r")
axs[0, 0].set_title("$f_1 (x) = x$")

x, y = create_plot(2)
axs[0, 1].plot(x, y, color = "b")
axs[0, 1].set_title("$f_2 (x) = x^2$")

x, y = create_plot(3)
axs[1, 0].plot(x, y, color = "g")
axs[1, 0].set_title("$f_3 (x) = x^3$")

x, y = create_plot(4)
axs[1, 1].plot(x, y, color = "k")
axs[1, 1].set_title("$f_4 (x) = x^4$")

# Wyświetlamy wykresy.
plt.show()