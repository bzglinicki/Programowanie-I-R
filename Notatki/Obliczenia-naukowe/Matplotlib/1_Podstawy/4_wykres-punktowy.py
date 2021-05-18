# Programowanie I R
# Pakiet matplotlib
# Wykres punktowy

import matplotlib.pyplot as plt

# Określamy punkty na wykresie, podając odpowiadająca sobie
# wartości współrzędnych x i y.
x = [1, 2, 3, 4, 5]
y = [4, 2, 1, 5, 3]

# Nanosimy punkty na wykres.
plt.scatter(x, y,
      color = "red",   # Kolor punktów.
      marker= "*",     # Typ punktów.
      s = 50           # Rozmiar punktów.
) 

# Podpisujemy osie.
plt.xlabel("Odcięta")
plt.ylabel("Rzędna")

# Nadajemy wykresowi tytuł.
plt.title("Punkty")

# Wyświetlamy wykres.
plt.show()