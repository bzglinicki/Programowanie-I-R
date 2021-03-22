# Programowanie I R
# Pakiet matplotlib
# Zapis do pliku - przykład 2.: wielostronicowy dokument PDF.

# Przykład pochodzi ze strony
#    https://matplotlib.org/3.1.1/gallery/misc/multipage_pdf.html

import math
import datetime
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

# Pomocnicze funkcje przygotowujące dane
# niezbędne do narysowania wykresów.
def plot_sq(): 
    x = [x * 0.1 for x in range(-100, 100)]
    y = []

    for x0 in x:
        y.append(x0**2)

    return (x, y)

def plot_sin(): 
    x = [x * 0.1 for x in range(-100, 100)]
    y = []

    for x0 in x:
        y.append(math.sin(x0))

    return (x, y)

# Tworzymy obiekt PdfPages reprezentujący plik PDF, w którym będziemy zapisywać
# wykresy. Użycie polecena "with" daje nam pewność, że plik ten zostanie
# poprawnie zamknięty po zakończeniu pracy, nawet jeśli w jej trakcie
# wystąpi jakiś problem.
with PdfPages('multipage_pdf.pdf') as pdf:
    # Ustalamy rozmiar pierwszego wykresu.
    plt.figure(figsize = (3, 3))

    # Rysujemy pierwszy wykres.
    plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], "r-o")
    plt.title("Wykres nr 1")

    # Zapisujemy pierwszy wykres do otwartego pliku PDF.
    pdf.savefig()

    # Zamykamy pierwszy wykres, przygotowując się tym samym do narysowania kolejnego.
    plt.close()

    # if LaTeX is not installed or error caught, change to `usetex=False`
    # plt.rc('text', usetex=True)

    # Powtarzamy te same czynności, by narysować drugi wykres.
    plt.figure(figsize = (8, 6))
    x, y = plot_sq()
    plt.plot(x, y, "b-")
    plt.title("Wykres nr 2")
    pdf.attach_note("Wykres y = sin(x)")  # Możemy modyfikować metadane
                                          # stron pliku PDF.
    pdf.savefig()
    plt.close()

    # Rysujemy trzeci wykres
    # plt.rc('text', usetex = False)
    fig = plt.figure(figsize = (4, 5))
    x, y = x, y = plot_sin()
    plt.plot(x, y, "go")
    plt.title("Wykres nr 3")
    pdf.savefig(fig)   # Możemy zdecydować, który z istniejących obiektów Figure jest
                       # zapisywany w pliku PDF. To istotne, gdy jest ich kilka.
    plt.close()

    # Możemy zapisać metadane pliku PDF.
    d = pdf.infodict()
    d["Title"] = "Przykład: Matplotlib i pliki PDF"
    d["Author"] = "Jouni K. Sepp\xe4nen"
    d["Subject"] = "Tworzenie wielostronicowego pliku PDF z wykresami"
    d["Keywords"] = "PdfPages multipage"
    d["CreationDate"] = datetime.datetime(2009, 11, 13)
    d["ModDate"] = datetime.datetime.today()