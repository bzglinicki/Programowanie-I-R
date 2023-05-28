# Programowanie I R
# Rozwiązania zadań - seria 12.
# Zadanie 1.

# Poniższy kod źródłowy został opracowany na podstawie kodu autorstwa Garbela Nervadofa,
# dostępnego pod adresem
#    https://levelup.gitconnected.com/solving-2d-heat-equation-numerically-using-python-3334004aa01a


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import sys


####################################################################################
# Inicjalizacja
####################################################################################

# Warunki początkowe i brzegowe (podane przez użytkownika).

T0 = float(sys.argv[1])   # Początkowa temperatura płytki.
T1 = float(sys.argv[2])   # Temperatura przyłożona do górnej krawędzi płytki.
T2 = float(sys.argv[3])   # Temperatura przyłożona do prawej krawędzi płytki.
T3 = float(sys.argv[4])   # Temperatura przyłożona do dolnej krawędzi płytki.
T4 = float(sys.argv[5])   # Temperatura przyłożona do lewej krawędzi płytki.


# Pozostałe parametry symulacji.

plate_size = 50   # Wymiary płytki.
t_max = 750       # Czas trwania symulacji.
alpha = 2         # Współczynnik alpha.
delta = 1         # Krok przestrzenny.
delta_t = (delta ** 2)/(4 * alpha)         # Krok czasowy.
gamma = (alpha * delta_t) / (delta ** 2)   # Współczynnik gamma.


# Model płytki. ####################################################################

# Tworzymy macierz reprezentującą płytkę. Jest to macierz trójwymiarowa - pierwszy
# wymiar reprezentuje czas, zaś pozostałe dwa - wymiary przestrzenne płytki.
T = np.empty((t_max, plate_size, plate_size))

# Narzucamy warunek początkowy: temperatura początkowa płytki wynosi T0.
T.fill(T0)

# Narzucamy warunki brzegowe: temperatury przyłożone do krawędzi płytki.
T[:, (plate_size - 1):, :] = T1
T[:, :, (plate_size - 1):] = T2
T[:, :1, 1:] = T3
T[:, :, :1] = T4


####################################################################################
# Ewolucja układu
####################################################################################

def SolveHeatEq():
    # Ta linia daje funkcji SolveHeatEq możliwość modyfikacji globalnej zmiennej T.
    global T
    
    # "Pętla czasowa": zmienna k numeruje kolejne chwile, rozmieszczone dyskretnie.
    for k in range(0, t_max-1, 1):
        # "Pętla przestrzenna": zmienna i numeruje kolejne punkty rozmieszczone
        # dyskretnie na osi Ox.
        for i in range(1, plate_size-1, delta):
            # "Pętla przestrzenna": zmienna j numeruje kolejne punkty rozmieszczone
            # dyskretnie na osi Oy.
            for j in range(1, plate_size-1, delta):
                T[k + 1, i, j] = gamma * (T[k][i+1][j] + T[k][i-1][j] + T[k][i][j+1] + T[k][i][j-1] - 4*T[k][i][j]) + T[k][i][j]


####################################################################################
# Animacja
####################################################################################

def PlotHeatMap(k):
    # Czyścimy bufor wykresu.
    plt.clf()

    # Określamy parametry wykresu: tytuł i opisy osi.
    plt.title(f"Temperatura w chwili $t$ = {k*delta_t:.3f} jednostek czasu")
    plt.xlabel("$x$")
    plt.ylabel("$y$")

    # Rysujemy wykres.
    plt.pcolormesh(T[k], cmap = plt.cm.jet, vmin = 0, vmax = 100)
    plt.colorbar()

    return plt


####################################################################################
# Główny kod programu
####################################################################################

# Rozwiązujemy równanie przewodnictwa cieplnego dla naszej płytki.
SolveHeatEq()

# Tworzymy i wyświetlamy animację.
anim = animation.FuncAnimation(plt.figure(), PlotHeatMap, interval = 1, frames = t_max, repeat = False)
plt.show()