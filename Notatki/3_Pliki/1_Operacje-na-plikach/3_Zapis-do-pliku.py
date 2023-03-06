# Programowanie I R
# Operacje na plikach: zapis

# W celu przeprowadzenia operacji zapisu do pliku musimy otworzyć ten plik w trybie
# zapisu (w), dołączania (a), tworzenia (x) lub edycji (r+).

# Należy zachować ostrożność przy stosowaniu trybu zapisu (w), ponieważ jeśli plik
# już istnieje, cała jego zawartość zostanie skasowana natychmiast po jego otwarciu.

# Sposób I: write() ****************************************************************

# Zapis łańcucha tekstowego (w trybie tekstowym, t) lub sekwencji danych binarnych
# (w trybie binarnym, b) do pliku jest możliwy dzięki metodzie write().

with open("plik.txt", "w", encoding = "utf-8") as f:
   f.write("Pierwsza linia.\n")
   f.write("Druga ")
   f.write("linia.\n")
   f.write("Trzecia linia.")

# Metoda write() zwraca liczbę znaków lub bitów zapisanych do pliku.

# Warto zwrócić uwagę, że metoda write() nie dodaje na końcu łańcucha tekstowego
# znaku nowej linii (w przeciwieństwie np. do znanej nam już funkcji print()).
# Pisząc do pliku tekstowego, sami musimy zadbać o umieszczenie w nim znaków
# nowej linii ("\n") w odpowiednich miejscach.

# Sposób II: writelines() **********************************************************

# Metoda writelines() przyjmuje jako argument listę i zapisuje do pliku jej kolejne
# elementy, jeden po drugim. Wbrew nazwie, funkcja ta nie umieszcza na końcu
# każdego elementu listy znaku nowej linii.

txt = ["Pierwsza linia.\n", "Druga linia.\n", "Trzecia linia."]

with open("plik.txt", "w", encoding = "utf-8") as f:
   f.writelines(txt)

# Sposób III: print() (tryb t) *****************************************************

# Istnieje możliwość przekierowania wyjścia funkcji print() tak, by wypisywała ona
# przekazany jej łańcuch tekstowy do pliku. Należy w tym celu wykorzystać argument
# file tej funkcji.

with open("plik.txt", "w", encoding = "utf-8") as f:
   print("Pierwsza linia.", file = f)
   print("Druga linia.", file = f)
   print("Trzecia linia.", end = "", file = f)