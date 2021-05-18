# Programowanie I R
# Pakiet matplotlib
# Zapis do pliku - przykład 1.: podstawy.

import matplotlib.pyplot as plt

# Określamy punkty na wykresie, podając odpowiadająca sobie
# wartości współrzędnych x i y.
x = [1, 2, 3, 4, 5]
y = [4, 2, 1, 5, 3]

# Rysujemy łamaną łączącą te punkty.
plt.plot(x, y)

# Podpisujemy osie.
plt.xlabel("Odcięta")
plt.ylabel("Rzędna")

# Nadajemy wykresowi tytuł.
plt.title("Łamana")

# Zapisujemy wykres w pliku PNG (grafika rastrowa).
plt.savefig("lamana.png",
            dpi = 300,           # Rozdzielczość (par. opcjonalny).
            transparent = True   # Przezroczystość tła (par. opcjonalny).
)

# Zapisujemy wykres w pliku JPG (grafika rastrowa).
plt.savefig("lamana.jpg",
            dpi = 300          # Rozdzielczość (par. opcjonalny).
)
# Można eksperymentować z zaawandowanymi opcjami (quality, optimize, progressive),
# pozwalającymi zmniejszyć rozmiar pliku przy zachowaniu porównywalnej jakości.

# Zapisujemy wykres w pliku SVG (grafika wektorowa).
plt.savefig("lamana.svg")

# Zapisujemy wykres w pliku PDF (grafika wektorowa).
plt.savefig("lamana.pdf")