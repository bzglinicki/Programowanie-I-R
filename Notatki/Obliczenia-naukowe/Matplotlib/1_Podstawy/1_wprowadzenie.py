# Programowanie I R
# Pakiet matplotlib
# Wprowadzenie. Pierwszy wykres

# Ładujemy moduł odpowiedzialny za rysowanie wykresów
# i nadajemy mu wygodny w użyciu alias "plt".
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
plt.title("Mój pierwszy wykres!")

# Wyświetlamy wykres.
plt.show()