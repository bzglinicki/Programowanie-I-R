# Programowanie I R
# Rozwiązania zadań - seria 12.
# Zadanie 2.

# Poniższy kod źródłowy został opracowany na podstawie kodu autorstwa Macieja Matyki,
# opublikowanego w książce "Symulacje komputerowe w fizyce", Wydanie II, Wydawnictwo
# Helion 2020. Kod ten dostępny jest bezpłatnie do pobrania na stronie Wydawnictwa
# Helion, pod adresem
#    https://helion.pl/pobierz-przyklady/sykof2/


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation


####################################################################################
# Inicjalizacja
####################################################################################

# Krok czasowy
dt = 0.045

# Liczba iteracji przy wyznaczaniu funkcji Psi' w jednym kroku czasowym
Niter = 5


# Siatka ###########################################################################

# Układ współrzędnych (dyskretnych): (x, y).

# Liczba oczek siatki w każdym wymiarze (siatka kwadratowa).
Nx = 70
Ny = 70

# Siatka przechowująca wartości funkcji falowej Psi (zespolone)
psi = np.zeros([Nx + 1, Ny + 1], dtype = complex)

# Siatka przechowująca wartości pomocniczej funkcji Psi' (zespolone)
psi_prime = np.zeros([Nx + 1, Ny + 1], dtype = complex)

# Siatka przechowująca wartości potencjału V
v = np.zeros([Nx + 1, Ny + 1])


# Potencjał ########################################################################

# Bariera potencjału.
for j in range(Ny + 1):
    v[int(Nx / 2), j] = 0.5


# Stan początkowy ##################################################################

# Paczka falowa (gaussowska).
sigma = Nx / 10.
x0 = 5
y0 = 35

for i in range(1, Nx):
    for j in range(1, Ny):
        pow = (- (i - x0) ** 2 - (j - y0) ** 2) / (sigma ** 2)
        psi[i, j] = np.exp(complex(pow, pow))


# Konfiguracja animacji ############################################################

X = np.arange(0, Nx + 1)
Y = np.arange(0, Ny + 1)
X, Y = np.meshgrid(X, Y)

# Przygotowanie wykresu stanu początkowego.
Z = psi.real**2 + psi.imag**2 + v

# Liczba klatek na sekundę
fps = 50

# Stylizacja wykresu
plot_args = {"cmap": cm.coolwarm, "linewidth": 0, "antialiased": False}


####################################################################################
# Ewolucja układu
####################################################################################

def SolveSchroedingerEq(a, b, plot):
    # Argumenty a i b nie mają znaczenia, pojawiają się wyłącznie dlatego,
    # że ich istnienia wymaga biblioteka Matplotlib.

    global psi, psi_prime

    # Mnożymy Psi przez 2 e^(- i V dt) dla uproszczenia kolejnego kroku.
    for i in range(1, Nx):
        for j in range(1, Ny):
            psi[i, j] *= 2 * np.exp(complex(0, - dt * v[i][j]))

    # Wyznaczamy Psi'.
    for k in range(Niter):
        for i in range(1, Nx):
            for j in range(1, Ny):
                re = psi[i][j].real - dt * (psi_prime[i+1][j].imag + psi_prime[i-1][j].imag + psi_prime[i][j-1].imag + psi_prime[i][j+1].imag - 4 * psi_prime[i][j].imag)
                im = psi[i][j].imag + dt * (psi_prime[i+1][j].real + psi_prime[i-1][j].real + psi_prime[i][j-1].real + psi_prime[i][j+1].real - 4 * psi_prime[i][j].real)
                psi_prime[i][j] = complex(re, im)
    
    # Wyznaczamy Psi.
    # Przez e^(-i V dt) wymnożyliśmy Psi już wcześniej; dla wygody pomnożyliśmy wówczas
    # Psi również przez 2, dlatego teraz dzielimy przez 2.
    for i in range(1, Nx):
        for j in range(1, Ny):
            psi[i][j] = psi_prime[i][j] - psi[i][j] / 2.
    
    # Moduł Psi - pojawi się na wykresie.
    Z = psi.real**2 + psi.imag**2 + v

    # Rysujemy wykres.
    plot[0].remove()
    plot[0] = ax.plot_surface(X, Y, Z, **plot_args)


####################################################################################
# Główny kod programu
####################################################################################

# Tworzymy i wyświetlamy animację.

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
plot = [ax.plot_surface(X, Y, Z, **plot_args)]
ani = animation.FuncAnimation(fig, SolveSchroedingerEq, 1, fargs = (3, plot), interval = 1000/fps)

plt.show()