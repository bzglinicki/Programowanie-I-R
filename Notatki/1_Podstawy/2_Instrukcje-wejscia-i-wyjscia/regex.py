# Programowanie I R
# Wyrażenia regularne (regular expressions, regex)

### -> DOKUMENTACJA:
###    https://docs.python.org/3/library/re.html
###
### -> OFICJALNY PRZEWODNIK:
###    https://docs.python.org/3/howto/regex.html
###
### -> przewodniki:
###    https://www.w3schools.com/python/python_regex.asp
###    https://developers.google.com/edu/python/regular-expressions
###    https://www.programiz.com/python-programming/regex

# Wyrażenie regularne to ciąg znaków określający wzorzec, z którym można porównywać
# łańcuchy tekstowe. Wzorzec taki może posłużyć np. do wyszukiwania w tekście tych
# fragmentów, które pasują do tego wzorca.

# Na przykład wyrażenie regularne
#    p...c
# reprezentuje łańcuch złożony z pięciu znaków, zaczynający się małą literą p oraz
# kończy małą literą c. Do wzorca tego pasują np. łańcuchy "pomoc", "pajac", "p000c",
# nie pasują zaś np. łańcuchy "prawy", "noc".

# Zasady tworzenia wyrażeń regularnych można znaleźć w dokumentacji i poradnikach, do
# których odnośniki umieszczone są na początku pliku.


#***********************************************************************************
# Korzystanie z wyrażeń regularnych
#***********************************************************************************

# W języku Python posługiwanie się wyrażeniami regularnymi jest możliwe między innymi
# dzięki modułowi re.

import re

# Moduł ten dostarcza pięciu funkcji pozwalających na wykorzystanie wyrażeń
# regularnych na cztery sposoby.


# Funkcja findall ******************************************************************

# Funkcja findall wyszukuje w zadanym łańcuchu tekstowym, przekazanym jej jako
# drugi argument, wszystkie ciągi znaków pasujące do wzorca przekazanego jako
# pierwszy argument, a następnie zwraca listę złożoną z tych ciągów.

# Ten wzorzec oznacza dowolnie długi łańcuch złożony wyłącznie z cyfr.
pattern = "\d+"

txt = "Ala ma 13 kotów, 8 żółwi i 12 ryb."
result = re.findall(pattern, txt) 
print(result)                                   # Wynik: ["13", "8", "12"].


# Funkcja split ********************************************************************

# Funkcja split wyszukuje w zadanym łańcuchu tekstowym, przekazanym jej jako
# drugi argument, wszystkie ciągi znaków pasujące do wzorca przekazanego jako
# pierwszy argument, a następnie dzieli ten łańcuch tekstowy na części w miejscach
# występowania pasujących ciągów i zwraca listę złożoną z tych części. Ciągi znaków
# pasujące do wzorca są usuwane.

# Ten wzorzec oznacza dowolnie długi łańcuch złożony wyłącznie z cyfr.
pattern = "\d+"

txt = "Ala ma 13 kotów, 8 żółwi i 12 ryb."
result = re.split(pattern, txt) 
print(result)        # Wynik: ["Ala ma ", " kotów, ", " żółwi i ", " ryb."]

# Funkcja split ma jeszcze jeden, trzeci argument o nazwie maxsplit. Określa on
# największą dopuszczalną liczbę cięć. Jeśli na przykład wartość argumentu
# maxsplit jest równa 3, funkcja split dokona cięć tylko w miejscu pierwszych
# trzech wystąpień ciągów pasujących do wzorca. Domyślna wartość argumentu
# maxsplit wynosi 0 i oznacza nieograniczoną liczbę cięć.

# Ten wzorzec oznacza dowolnie długi łańcuch złożony wyłącznie z cyfr.
pattern = "\d+"

txt = "Ala ma 13 kotów, 8 żółwi i 12 ryb."

# maxsplit = 1 - cięcie tylko przy pierwszym wystąpieniu ciągu pasującego do wzorca.
result = re.split(pattern, txt, 1) 
print(result)             # Wynik: ["Ala ma ", " kotów, 8 żółwi i 12 ryb."]


# Funkcje sub i subn ***************************************************************

# Funkcja sub wyszukuje w zadanym łańcuchu tekstowym, przekazanym jej jako trzeci
# argument, wszystkie ciągi znaków pasujące do wzorca przekazanego jako pierwszy
# argument, a następnie zastępuje je ciągiem znaków określonym przez wartość jej
# drugiego argumentu i zwraca utworzony w ten sposób łańcuch tekstowy.

# Ten wzorzec oznacza dowolnie długi łańcuch złożony wyłącznie z cyfr.
pattern = "\d+"

replace = "dużo"
txt = "Ala ma 13 kotów, 8 żółwi i 12 ryb."
result = re.sub(pattern, replace, txt) 
print(result)        # Wynik: "Ala ma dużo kotów, dużo żółwi i dużo ryb.".

# Funkcja sub może przyjąć dodatkowy, czwarty argument o nazwie count. Określa on
# największą dopuszczalną liczbę zamian. Jeśli na przykład wartość argumentu
# count jest równa 3, funkcja sub dokona zastąpienia tylko pierwszych trzech wystąpień
# ciągów pasujących do wzorca. Domyślna wartość argumentu count wynosi 0 i oznacza
# nieograniczoną liczbę zamian.

# Ten wzorzec oznacza dowolnie długi łańcuch złożony wyłącznie z cyfr.
pattern = "\d+"

replace = "dużo"
txt = "Ala ma 13 kotów, 8 żółwi i 12 ryb."
result = re.sub(pattern, replace, txt, 1) 
print(result)       # Wynik: "Ala ma dużo kotów, 8 żółwi i 12 ryb.".

# Funkcja subn działa niemal identycznia, jak funkcja sub. Jedyna różnica polega na tym,
# że funkcja subn zwraca krotkę złożoną z nowego łańcucha tekstowego, otrzymanego
# w wyniku wykonania zastąpień, oraz liczby całkowitej określającej ilość zastąpień.

# Ten wzorzec oznacza dowolnie długi łańcuch złożony wyłącznie z cyfr.
pattern = "\d+"

replace = "dużo"
txt = "Ala ma 13 kotów, 8 żółwi i 12 ryb."
result = re.subn(pattern, replace, txt) 
print(result)   # Wynik: ("Ala ma dużo kotów, dużo żółwi i dużo ryb.", 3).


# Funkcja search *******************************************************************

# Funkcja search wyszukuje w zadanym łańcuchu tekstowym, przekazanym jej jako drugi
# argument, pierwszy ciąg znaków pasujący do wzorca przekazanego jako pierwszy
# argument, a następnie zwraca obiekt klasy Match związany z tym dopasowaniem
# (patrz niżej) lub wartość None, jeśli odpowiedni ciąg nie został znaleziony.

# Ten wzorzec oznacza dowolnie długi łańcuch złożony wyłącznie z cyfr.
pattern = "\d+"

txt = "Ala ma 13 kotów, 8 żółwi i 12 ryb."
result = re.search(pattern, txt) 

if result:
   print("Znaleziono wystąpienie wzorca!")
else:
   print("Nie znaleziono żadnego wystąpienie wzorca!")

# Wynik: Znaleziono wystąpienie wzorca!

# Zwracany przez funkcję search objekt klasy Match zawiera szczegółowe informacje
# o odnalezionym dopasowaniu oraz udostępnia pola i metody pozwalające na odczyt
# tych informacji, między innymi:
#    - group   - metoda, zwraca odnaleziony ciąg znaków,
#    - start   - metoda, zwraca indeks tego znaku oryginalnego łańcucha,
#                który rozpoczyna odnaleziony ciąg znaków,
#    - end     - metoda, zwraca indeks tego znaku oryginalnego łańcucha,
#                który kończy odnaleziony ciąg znaków,
#    - span    - metoda, zwraca krotkę złożoną z wartości zwracanej przez
#                funkcję start oraz wartości zwracanej przez funkcję end,
#    - string  - pole, zawiera oryginalny łańcuch tekstowy.

# Ten wzorzec oznacza dowolnie długi łańcuch złożony wyłącznie z cyfr.
pattern = "\d+"

txt = "Ala ma 13 kotów, 8 żółwi i 12 ryb."
result = re.search(pattern, txt) 

if result:
   print("Znaleziono wystąpienie wzorca!")
   print()
   print(f"Znaleziony ciąg znaków: \"{result.group()}\".")
   print(f"Oryginalny łańcich: \"{result.string}\".")
   print(f"Indeks początku znalezionego ciągu: {result.start()}.")
   print(f"Indeks końca znalezionego ciągu: {result.end()}.")
else:
   print("Nie znaleziono żadnego wystąpienie wzorca!")