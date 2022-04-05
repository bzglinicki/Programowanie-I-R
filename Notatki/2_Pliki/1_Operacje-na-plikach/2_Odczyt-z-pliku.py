# Programowanie I R
# Operacje na plikach: odczyt

# W celu przeprowadzenia operacji odczytu z pliku, musimy otworzyć ten plik w trybie
# odczytu (r) lub edycji (w+, a+, x+).

# Istnieje kilka sposobów odczytu zawartości pliku. Przedstawimy je na przykładzie
# pliku plik.txt o następującej zawartości:
#    Pierwsza linia.
#    Druga linia.
#    Trzecia linia.

# Sposób I: read() *****************************************************************

# Metoda read() odczytuje kolejne znaki (w trybie tekstowym, t) lub kolejne bity
# (w trybie binarnym, b), począwszy od aktualnego położenia kursora. Przyjmuje ona
# argument size, określający, ile znaków lub bitów ma odczytać; jeśli nie określimy
# wartości tego argumentu, metoda ta odczytuje plik aż do napotkania jego końca. Po
# zakończeniu odczytu metoda ustawia kursor na końcu odczytanego fragmentu pliku
# i zwraca jako swoją wartość odczytany łańcuch tekstowy lub dane binarne.

with open("plik.txt", "r", encoding = "utf-8") as f:
   # Kursor jest początkowo na początku pliku (tak jest zawsze w trybie r).
   txt = f.read(4)    # Odczyt czterech znaków i przeniesienie kursosa
                      # za te znaki (czyli przed piąty znak).
   print(txt)         # Wynik: "Pier".

   txt = f.read(3)    # Odczyt kolejnych trzech znaków i przeniesienie kursosa
                      # za te znaki.
   print(txt)         # Wynik: "wsz".

   txt = f.read()     # Odczyt reszty pliku (od aktualnego położenia kursora do końca pliku)
                      # i przeniesienie kursora na koniec pliku.
   print(txt)         # Wynik: "a linia.
                      #         Druga linia.
                      #         Trzecia linia."

   txt = f.read()     # Kursor jest obecnie na końcu pliku, więc nic nie zostanie odczytane.
   print(txt)         # Wynik: "" (pusty łańcuch tekstowy).

   # Położeniem kursora możemy sterować za pomocą dwóch metod:
   #    tell()   - zwraca liczbę określającą aktualną pozycję kursora,
   #    seek(n)  - ustawia kursor na pozycji określonej liczbą n.
   # Liczba określająca pozycję kursora informuje, za którym znakiem (w trybie tekstowym, t),
   # lub bitem (w trybie binarnym, b) znajduje się kursor. I tak, 0 oznacza, że kursor
   # znajduje się na początku pliku, 1 - za pierwszym znakiem etc.

   i = f.tell()       # Zwraca aktualne położenie kursora. Kursor jest na końcu pliku,
                      # w wyniku otrzymamy zatem ilość znaków w pliku.
   print(i)           # Wynik: 45.

   f.seek(0)          # Ustawia kursor na pozycji 0, czyli na początku pliku.
   i = f.tell()       # Tym razem kursor jest na początku pliku, otrzymamy zatem 0.
   print(i)           # Wynik: 0.

   txt = f.read()     # Kursor jest obecnie na początku pliku, więc to polecenie spowoduje
                      # odczyt całej zawartości pliku i przeniesienie kursora na jego koniec.
   print(txt)         # Wynik: "Pierwsza linia.
                      #         Druga linia.
                      #         Trzecia linia."

# Sposób II: Pętla for (tryb t) ****************************************************

# Możemy odczytywać zawartość pliku tekstowego linia po linii, stosując pętlę for.

with open("plik.txt", "r", encoding = "utf-8") as f:
   for line in f:
      print(line, end = "")

# W kolejnych iteracjach pętli zmienna line zawiera kolejne linie pliku plik.txt.
# Każda linia pliku tekstowego zawiera oczywiście na końcu znak nowej linii,
# dlatego znak ten jest również umieszczany na końcu łańcucha tekstowego będącego
# wartością zmiennej line (z tego powodu zmieniliśmy domyślny koniec linii w funkcji
# print() na pusty łańcuch, inaczej znak nowej linii byłby wypisywany dwukrotnie).

# Sposób III: readline() (tryb t) **************************************************

# Metoda readline() odczytuje aktualną linię pliku tekstowego, począwszy od miejsca,
# w którym znajduje się kursor, aż do znaku nowej linii włącznie, a następnie
# ustawia kursor na początku kolejnej linii. Tak więc, wielokrotne wywoływanie
# tej metody pozwala odczytywać kolejne linie pliku.

with open("plik.txt", "r", encoding = "utf-8") as f:
   line = f.readline()
   print(line, end = "")   # Wynik: "Pierwsza linia."

   line = f.readline()
   print(line, end = "")   # Wynik: "Druga linia."

   line = f.readline()
   print(line, end = "")   # Wynik: "Trzecia linia."

   # Kursor jest teraz na końcu pliku.
   line = f.readline()
   print(line, end = "")   # Wynik: "" (pusty łańcuch tekstowy).

# Sposób IV: readlines() (tryb t) **************************************************

# Metoda readlines() zwraca w postaci listy kolejne linie pliku, począwszy od miejsca,
# w którym aktualnie znajduje się kursor, aż do końca pliku. Gdy kursor ustawiony
# jest na końcu pliku, metoda ta zwraca pustą listę.

   with open("plik.txt", "r", encoding = "utf-8") as f:
       lines = f.readlines()
       print(lines)
       # Wynik: ["Pierwsza linia.", "Druga linia.", "Trzecia linia."]
   
# W przypadku dużych plików sposób ten powinien być stosowany bardzo ostrożnie, 
# wczytanie do pamięci jednocześnie bardzo wielu linii pliku może doprowadzić
# do wystąpienia wyjątku.

# Sposób V: Iterowanie po pliku binarnym (tryb b) **********************************

# Spośród przedstawionych powyżej sposobów pierwszy jest uniwersalny, można go
# z równym powodzeniem stosować zarówno w przypadku plików tekstowych, jak
# i binarnych. Pozostałe sposoby wykorzystują pojęcie "linii", ich działanie jest
# uzależnione od występowania w pliku znaków końca linii. Może się zdarzyć, że
# w pliku binarnym wystąpi sekwencja bitów odpowiadająca temu znakowi, jednak
# będzie to raczej przypadek, stosowanie metod II - IV w przypadku plików binarnych
# nie ma więc sensu.

# W celu odczytu zawartości plików binarnych należy zatem posługiwać się metodą
# read() (sposób I). To, czy odczytujemy cały plik od razu, czy też operujemy na
# jego fragmentach, powinno zależeć od jego struktury (określonej na przykład
# przez specyfikację dango formatu pliku) i naszych celów.

# Możemy iterować po zawartości pliku binarnego (na wzór sposobu II), nie mając
# jednak do dyspozycji pojęcia linii, musimy określić, jakiego rozmiaru fragmenty
# pliku chcemy jednocześnie przetwarzać. Taki iteracyjny odczyt pliku binarnego
# można zrealizować na przykład stosując pętlę while.

with open("plik.txt", "rb") as f:
   size = 200
   while True:
      data = f.read(size)
      if not data:
         break
      print(data)

# Można też napisać funkcję generującą, która pozwoli nam odczytywać zawartość
# plików binarnych za pomocą pętli for (analogicznie jak dla plików tekstowych
# w sposobie II):

def bin_read(f, size = 1024*64):
    data = f.read(size)
    while data:
        yield data
        data = f.read(size)

with open("plik.txt", "rb") as f:
    for data in bin_read(f):
        print(data)