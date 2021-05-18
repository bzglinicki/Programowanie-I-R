# Programowanie I R
# Pakiet matplotlib
# Wykres funkcji

import math
import matplotlib.pyplot as plt

# Określamy dyskretny zbiór argumentów i obliczamy wartości funkcji.
x = [x * 0.1 for x in range(0, 70)]
y = []
for x0 in x:
    y.append(math.sin(x0))

# Wykreślamy funkcję. Tak naprawdę rysujemy tu łamaną złożoną
# z bardzo wielu krótkich odcinków.
plt.plot(x, y)

# Podpisujemy osie. Możemy stosować zapis matematyczny z LaTeX.
plt.xlabel("$x$")
plt.ylabel("$y$")

# Nadajemy wykresowi tytuł.
plt.title(r"$y = \sin x$")

# Wyświetlamy wykres.
plt.show()