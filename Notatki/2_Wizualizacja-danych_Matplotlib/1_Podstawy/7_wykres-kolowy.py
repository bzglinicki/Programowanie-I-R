# Programowanie I R
# Pakiet matplotlib
# Wykres kołowy

import matplotlib.pyplot as plt

# Etykiety.
labels = ["A", "B", "C", "D", "E"]
  
# Wartości.
values = [100, 300, 200, 500, 400]
  
# Kolory.
colors = ["red", "green", "blue", "yellow", "purple"]
  
# Rysujemy wykres kołowy.
plt.pie(values, labels = labels, colors = colors,  
        startangle = 90, shadow = True, explode = (0, 0, 0.3, 0, 0), 
        radius = 1.2, autopct = "%1.1f%%"
)
  
# Umieszczamny na wykresie legendę.
plt.legend()

# Wyświetlamy wykres.
plt.show()