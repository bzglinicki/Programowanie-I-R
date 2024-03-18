# Programowanie I R
# Rozwiązania zadań - seria 4.
#
# Zadanie 3. Balansowanie ciągów nawiasów.
# Program "brackets".

import sys


#***********************************************************************************
# Funkcje wykonujące poszczególne zadania
#***********************************************************************************

# brackets check *******************************************************************

# Do rozwiązania tego problemu wykorzystamy pojęcie stosu (ang. stack), czyli
# struktury danych dopuszczającej zasadniczo tylko dwie operacje: „odłożenie” nowych
# danych na „wierzch” oraz „zdjęcie” danych z „wierzchu”. Ideę stosu można łatwo
# zrozumieć, wyobrażając sobie jakiś rzeczywisty stos, np. zbiór położonych jedna
# na drugiej książek. Nową książkę możemy położyć jedynie na wierzchu stosu, możemy
# też zdjąć ze stosu wyłącznie książkę leżącą na jego wierzchu. Sięgnięcie po
# książkę znajdującą się poniżej wierzchu wymaga zdejmowania po kolei wszystkich
# książek, które leżą wyżej. Stos, choć jest niezwykle prostą strukturą danych,
# znalazł wiele zastosowań i odgrywa niezwykle ważną rolę w systemach informatycznych.

# Język Python nie posiada natywnej implementacji stosu, możemy jednak łatwo stworzyć
# własną implementację, wykorzystując do tego celu listę. Odłożenie na stos nowego
# obiektu będzie odpowiadało umieszczeniu go na końcu listy (metoda append), zdjęcie
# obiektu ze stosu – usunięciu ostatniego elementu listy (metoda pop), zaś odczyt
# wartości obiektu na wierzchu stosu – odczytowi wartości ostatniego elementu listy
# (operator indeksowania, czyli nawiasy kwadratowe).

# W celu ustalenia, czy dany ciąg nawiasów jest zbalansowany, będziemy przeglądać
# go element po elemencie. Za każdym razem, gdy napotkamy jeden z nawiasów otwiera-
# jących, odłożymy go na stos, gdy zaś natrafimy na któryś z nawiasów zamykających,
# sprawdzimy, czy na wierzchu stosu znajduje się odpowiadający mu nawias otwiera-
# jący. Jeśli tak będzie, ta para nawiasów jest poprawnie zagnieżdżona, zdejmiemy
# zatem nawias otwierający ze stosu i będziemy kontynuować przeglądanie ciągu;
# w przeciwnym przypadku ciąg z pewnością nie jest zbalansowany (nawiasy nie są
# bowiem poprawnie zagnieżdżone lub – gdy stos okaże się pusty – nawiasów zamyka-
# jących jest więcej niż otwierających). Gdy uda nam się dotrzeć do końca ciągu,
# znajdując zawsze na wierzchu stosu właściwy nawias, a po przejrzeniu całego ciągu
# stos będzie pusty, ciąg jest zbalansowany; w przeciwnym razie ciąg zbalansowany
# nie jest.

# Wszelkie znaki niebędące nawiasami zignorujemy. Dzięki temu nasza metoda sprawdzi
# się również w badaniu poprawności rozstawienia nawiasów np. w wyrażeniach matema-
# tycznych, tekstach literackich czy kodzie programów komputerowych.

def BracketsCheck(s):
   brackets_opening = ["[", "{", "("]   # Dopuszczalne nawiasy otwierające.
   brackets_closing = ["]", "}", ")"]   # Dopuszczalne nawiasy zamykające.
   stack = []   # Stos.
   
   for c in s:   # Przeglądamy ciąg nawiasów s element po elemecie.
      if c in brackets_opening:    # Jeśli dany nawias jest nawiasem otwierającym...
         stack.append(c)        # ...odkładamy go na stosie.
      elif c in brackets_closing: # Jeśli dany nawias jest nawiasem zamykającym...
         i = brackets_closing.index(c)   # ...zapisujemy jego pozycję na liście nawiasów...
         # ...i sprawdzamy, czy na wierzchu stosu znajduje się odpowiadający mu
         # nawias otwierający. Jeśli tak...
         if (len(stack) > 0) and (stack[len(stack)-1] == brackets_opening[i]):
            stack.pop()   # ...zdejmujemy nawias otwierający ze stosu i idziemy dalej.
         else:   # Jeśli jednak nie...
            return False   # ...ciąg nawiasów nie jest zbalansowany.
      # Nie rozważamy sytuacji, gdy znak c nie jest ani nawiasem otwierającym, ani
      # nawiasem zamykającym, zatem wszystkie znaki niebędące którymś z dopuszczalnych
      # nawiasów zostaną zignorowane.
   
   if len(stack) == 0:   # Jeśli po przeanalizowaniu całego ciągu stos jest pusty...
      return True        # ...ciąg jest zbalansowany.
   else:                 # W przeciwnym przypadku...
      return False       # ...ciąg nie jest zbalansowany.

"""   KOMENTARZ
Istnieją też inne równie proste sposoby rozwiązania tego problemu. Moglibyśmy na
przykład przeglądać ciąg nawiasów wielokrotnie, za każdym razem usuwając napotkane
w nim pary stojących obok siebie i odpowiadających sobie nawiasów (czyli podciągi
„()”, „[]” i „{}”). Gdybyśmy otrzymali w ten sposób ciąg pusty, oznaczałoby to, że
wyjściowy ciąg był zbalansowany. Przykładowy kod realizujący ten algorytm:

def BracketsCheck(s):
   brackets = ["()", "[]", "{}"]
   while any(b in s for b in brackets):
      for bracket in brackets:
         s = s.replace(bracket, "")
   return not s

Rozwiązanie, które wybraliśmy, jest jednak bardzo pouczające, wykorzystuje bowiem stos,
ponadto – jak już wspominaliśmy – uogólnia się na sytuacje, w których badany łańcuch
tekstowy zawiera też znaki inne niż nawiasy.
"""


# brackets fix *********************************************************************

# Będziemy przeglądać ciąg nawiasów element po elemencie. Gdy natrafimy na nawias
# otwierający, w dalszej części ciągu musi się znaleźć odpowiadający mu nawias
# zamykający, zwiększymy zatem wartość licznika brakujących nawiasów zamykających
# o jeden; gdy z kolei napotkamy nawias zamykający, zmniejszymy wartość tego licznika
# o jeden. Jeśli jednak trafimy na nawias zamykający, a licznik brakujących nawiasów
# zamykających będzie wskazywał zero, będzie to oznaczało, że we wcześniejszej części
# ciągu zabrakło nawiasu otwierającego sparowanego z napotkanym właśnie nawiasem
# zamykającym, zwiększymy więc wartość licznika brakujących nawiasów otwierających
# o jeden. Po przejrzeniu całego ciągu suma wartości obu wspomnianych liczników będzie
# liczbą brakujących nawiasów.

# Znaki niebędące nawiasami będą ignorowane, dzięki czemu nasz algorytm okaże się
# skuteczny również w przypadku ciągów zawierających dodatkowe znaki (podobnie jak
# algorytm zastosowany w funkcji bracketsCheck).

# Warto zwrócić uwagę na fakt, że rozwiązanie polegające na obliczeniu modułu różnicy
# liczby nawiasów otwierających i liczby nawiasów zamykających nie byłoby poprawne,
# istotna jest bowiem nie tylko liczba nawiasów, ale też właściwe ich zagnieżdżenie.
# Na przykład ciąg „)(” wymaga dopisania dwóch nawiasów, by otrzymać zbalansowany
# ciąg „()()”, zaś różnica liczby nawiasów otwierających i liczby nawiasów zamykających
# wynosi w jego przypadku zero.

def BracketsFix(s):
   opening = 0   # Licznik brakujących nawiasów otwierających.
   closing = 0   # Licznik brakujących nawiasów zamykających.

   for i in range(len(s)):   # Przeglądamy ciąg nawiasów element po elemencie.
      if s[i] == "(":        # Gdy napotkamy nawias otwierający...
         closing += 1        # ...zwiększamy licznik brakujących nawiasów zamykających o 1.
      elif s[i] == ")":      # Gdy z kolei natrafimy na nawias zamykający...
         if closing > 0:     # ...i brakuje nawiasów zamykających...
            closing -= 1     # ...zmniejszamy licznik brakujących nawiasów zamykających o 1.
         else:               # Jeśli jednak nawiasów zamykających nie brakuje...
            opening += 1     # ...zwiększamy licznik brakujących nawiasów otwierających o 1.
   
   return opening + closing  # Zwracamy liczbę wszystkich brakujących nawiasów.


# brackets list ********************************************************************

# Do rozwiązania tego problemu wykorzystamy rekurencję. W funkcji bracketsList
# utworzymy najpierw pustą listę res, na której będą zapisywane kolejne ciągi nawiasów,
# a następnie wywołamy pomocniczą funkcję bl, która będzie generowała ciągi o żądanej
# długości i zapisywała je na liście res.

# Funkcja bl przyjmuje następujące parametry:
#    str – łańcuch tekstowy zawierający budowany właśnie ciąg nawiasów,
#    opening – liczba nawiasów otwierających w ciągu str,
#    closing – liczba nawiasów zamykających w ciągu str,
#    n – parametr określający żądaną liczbę nawiasów każdego z typów (ciąg ma mieć
#        długość 2n),
#    res – lista, na której mają się znaleźć generowane ciągi.

# Funkcja bl sprawdza na początku, czy ciąg zapisany w zmiennej str jest już gotowy,
# to znaczy czy ma żądaną długość – jest tak wtedy, gdy liczby nawiasów otwierających
# i zamykających są równe n; w praktyce wystarczy sprawdzić , czy liczba nawiasów
# zamykających wynosi n. Gdy ciąg jest gotowy, funkcja bl zapisuje go na liście res
# i kończy swoje działanie, w przeciwnym razie kontynuuje budowanie ciągu. Proces
# budowania ciągu polega na dopisaniu do niego jednego z nawiasów (otwierającego lub
# zamykającego), o ile nawiasów danego typu nie jest już wystarczająco dużo, a następnie
# rekurencyjnym wywołaniu funkcji bl z tak „rozbudowanym” ciągiem. Powstanie w ten sposób
# drzewo rekurencyjnych wywołań funkcji bl, różne ścieżki w obrębie tego drzewa wygenerują
# różne zbalansowane ciągi o zadanej długości, dając nam ostatecznie zbiór wszystkich
# takich ciągów.

def BracketsList(n):
   if n > 0:                 # Problem ma sens tylko dla n > 0.
      res = []               # Wynikowa lista wygenerowanych ciągów.
      BL("", 0, 0, n, res)   # Wywołanie funkcji pomocniczej.
      return res             # Po wywołaniu funkcji bl lista res zawiera szukane ciągi.
   return []                 # Gdy n <= 0, zwracamy pustą listę.

# Funkcja pomocnicza
def BL(str, opening, closing, n, res):
   if closing == n:      # Gdy ciąg ma już żądaną długość...
      res.append(str)    # ...dopisujemy go do wynikowej listy ciągów.
   else:                 # Gdy w ciągu wciąż brakuje nawiasów...
      if opening < n:    # ...jeśli nadal jest za mało nawiasów otwierających...
         BL(str + "(", opening + 1, closing, n, res)   # dodajemy nawias otwierający,
      if opening > closing:   # ...jeśli nawiasów zamykających wciąż jest mniej niż otwierających...
         BL(str + ")", opening, closing + 1, n, res)   # dodajemy nawias zamykający.


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

if len(sys.argv) != 3:
   print("Błąd! Niepoprawna liczba argumentów.")
   quit()

if sys.argv[1] == "check":
   print(f"Ciąg nawiasów\n   {sys.argv[2]}")
   if BracketsCheck(sys.argv[2]):
      print("jest zbalansowany.")
   else:
      print("nie jest zbalansowany.")
elif sys.argv[1] == "fix":
   print(f"Ciąg nawiasów\n   {sys.argv[2]}")
   n = BracketsFix(sys.argv[2])
   if n == 0:
      print("jest zbalansowany.")
   elif n == 1:
      print(f"będzie zbalansowany po dopisaniu 1 nawiasu.")
   else:
      print(f"będzie zbalansowany po dopisaniu {n} nawiasów.")
elif sys.argv[1] == "list":
   n = int(sys.argv[2])
   if n <= 0:
      print("Błąd! Liczba nawiasów w ciągu musi być dodatnia.")
      quit()
   elif n == 1:
      print("Ciąg zbalansowany zbudowany z 1 pary nawiasów:")
   else:
      print(f"Ciągi zbalansowane zbudowane z {n} par nawiasów:")
   for s in BracketsList(int(sys.argv[2])):
      print("   " + s)
else:
   print("Błąd! Nieprawidłowe argumenty.")