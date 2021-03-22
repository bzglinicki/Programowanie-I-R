# Programowanie I R
# Pakiet matplotlib
# Wiele krzywych na jednym wykresie

import matplotlib.pyplot as plt

# Określamy pierwszą łamaną i rysujemy ją, nadając jej etykietę.
x1 = [1, 2, 3, 4, 5]
y1 = [4, 2, 1, 5, 3]
plt.plot(x1, y1, label = "Krzywa nr 1")

# Określamy drugą łamaną i rysujemy ją, nadając jej etykietę.
x2 = [1, 2, 3, 4, 5]
y2 = [2, 5, 3, 1, 4]
plt.plot(x2, y2, label = "Krzywa nr 2")

# Podpisujemy osie.
plt.xlabel("Odcięta")
plt.ylabel("Rzędna")

# Nadajemy wykresowi tytuł.
plt.title("Dwie krzywe na jednym wykresie")

# Umieszczamy na wykresie legendę. Krzywe zostaną w niej podpisane etykietami,
# które im nadaliśmy, rysując je (argument "label" metody "plot").
plt.legend()

# Wyświetlamy wykres.
plt.show()