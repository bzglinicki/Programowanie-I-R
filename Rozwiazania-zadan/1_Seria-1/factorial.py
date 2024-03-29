# Programowanie I R
# Zadanie factorial

# Funkcja ifactorial()
#    Iteracyjne obliczanie silni liczby naturalnej.
#
#    Argumenty:
#       n - liczba naturalna.
#
#    Wynik:
#       Liczba naturalna.
#          Silnia liczby n.
def ifactorial(n):
    if n <= 1: return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Funkcja rfactorial()
#    Rekurencyjne obliczanie silni liczby naturalnej.
#
#    Argumenty:
#       n - liczba naturalna.
#
#    Wynik:
#       Liczba naturalna.
#          Silnia liczby n.
def rfactorial(n):
   if n <= 1:
       return 1
   else:
       return n * rfactorial(n - 1)

# Główny program
import time

n = int(input("Podaj liczbę naturalną: "))

# Obliczenie silni - algorytm iteracyjny
i_start = time.perf_counter_ns()
result_i = ifactorial(n)
i_stop = time.perf_counter_ns()

print(f"Silnia liczby {n} - algorytm iteracyjny:")
print(f"   Wynik: {result_i}.")
print(f"   Czas wykonania: {i_stop - i_start} ns.")

# Obliczenie silni - algorytm rekurencyjny
r_start = time.perf_counter_ns()
result_r = rfactorial(n)
r_stop = time.perf_counter_ns()

print(f"Silnia liczby {n} - algorytm rekurencyjny:")
print(f"   Wynik: {result_r}.")
print(f"   Czas wykonania: {r_stop - r_start} ns.")