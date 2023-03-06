# Programowanie I R
# Pakiet matplotlib
# Dostosowywanie wykresów

import matplotlib.pyplot as plt

# Określamy punkty na wykresie, podając odpowiadająca sobie
# wartości współrzędnych x i y.
x = [1, 2, 3, 4, 5]
y = [4, 2, 1, 5, 3]

# Rysujemy łamaną łączącą te punkty, stosując dodatkowe argumenty
# dostosowujące jej wygląd.
plt.plot(x, y,
      color = "blue",            # Kolor linii.
      linestyle = "dashed",      # Styl linii.
      linewidth = 3,             # Grubość linii.
      marker = "o",              # Styl markerów oznaczających wierzchołki łamanej.
      markerfacecolor = "red",   # Kolor markerów.
      markersize = 12            # Wielkość markerów.
)

# Ustalamy zakres na osiach, odpowiednio, Ox i Oy.
plt.xlim(-1, 8)
plt.ylim(-1, 7)

# Podpisujemy osie.
plt.xlabel("Odcięta")
plt.ylabel("Rzędna")

# Nadajemy wykresowi tytuł.
plt.title("Piękna łamana")

# Wyświetlamy wykres.
plt.show()