# Programowanie I R
# Rozwiązania zadań - seria 3.
# Zadanie 2.  words - Liczenie wyrazów.

# Wykorzystując funkcję input wczytujemy ze standardowego wejścia łańcuch tekstowy
# - zgodnie z treścią zadania powinien on być ciągiem wyrazów oddzielonych spacjami.
# Następnie na wyniku działania funkcji input (czyli wczytanym łańcuchu tekstowym)
# wywołujemy metodę split z argumentem " " - dokona ona "pocięcia" tego łańcucha
# w miejscach występowania spacji i zwróci listę złożoną z jego fragmentów powstałych
# w wyniku tego "pocięcia", a więc z pojedynczych wyrazów.
words = input().split(" ")

# W celu lepszego zrozumienia powyższej instrukcji zauważmy, że można zapisać ją
# w postaci dwóch instrukcji, z których każda realizuje tylko jedno zadanie:
#   words_str = input()
#   words = words_str.split(" ")


# Wykorzystując wyrażenie słownikotwórcze (ang. dictionary comprehension) tworzymy słownik
# o następującej strukturze: każdy klucz tego słownika jest jednym z wyrazów (elementem
# listy words), zaś wartość odpowiadająca temu kluczowi - liczbą wystąpień tego wyrazu
# na liście words.
words_count = {word:words.count(word) for word in words}

# Wypisujemy na standardowe wyjście wczytane wyrazy w kolejności alfabetycznej, podając przy
# każdym z nich liczbę jego wystąpień. Metoda items() zwraca elementy słownika w postaci listy
# krotek, zaś funkcja sorted sortuje tę listę po pierwszym elemencie krotki.
for word, count in sorted(words_count.items()):
    print(f"{word} {count}")