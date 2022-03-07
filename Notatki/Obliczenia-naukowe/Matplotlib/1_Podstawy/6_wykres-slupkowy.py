# Programowanie I R
# Pakiet matplotlib
# Wykres słupkowy

import matplotlib.pyplot as plt

# Współrzędne x lewych brzegów kolejnych słupków.
x = [1, 2, 3, 4, 5]

# Wysokości kolejnych słupków.
y = [100, 300, 200, 500, 400]

# Etykiety kolejnych słupków.
labels = ["A", "B", "C", "D", "E"]

# Rysujemy wykres słupkowy.
plt.bar(x, y, tick_label = labels, 
        width = 0.8, color = ["red", "blue"]
) 

# Podpisujemy osie.
plt.xlabel("Etykieta")
plt.ylabel("Wartość")

# Nadajemy wykresowi tytuł.
plt.title("Wykres słupkowy")

# Wyświetlamy wykres.
plt.show()