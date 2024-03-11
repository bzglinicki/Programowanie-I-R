# Programowanie I R
# Rozwiązania zadań - seria 3.
# Zadanie 1. lotto - Losowanie liczb.


import random

# Tworzymy pusty zbiór.
lotto = set()

# Losujemy liczby całkowite z przedziału [1, 49] i dodajemy je do zbioru lotto
# dopóki ilość elementów tego zbioru jest mniejsza od 6.
while len(lotto) < 6:
    lotto.add(random.randint(1, 49))

# Wypisujemy zbiór lotto na standardowe wyjście.
#   Instrukcja sorted(lotto) zwraca listę złożoną z posortowanych rosnąco
#   elementnów zbioru lotto. W pętli for przebiegamy po elementach tej listy,
#   wypisując każdy z nich na standardowe wyjście. Argument end funkcji print
#   o wartości " " zapewnia, że funkcja ta umieści na końcu wypisywanego
#   łańcucha spację zamiast znaku nowej linii - dzięki temu liczby będą
#   wypisane w jednej linii i oddzielone spacjami.
for k in sorted(lotto):
    print(k, end=" ")