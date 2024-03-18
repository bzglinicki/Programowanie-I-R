# Programowanie I R
# Rozwiązania zadań - seria 4.
#
# Zadanie 2. Palindromy.
# Program "palindrome".

import sys


#***********************************************************************************
# Funkcja is_palindrome
#***********************************************************************************

def is_palindrome(str):
   # Tworzymy listę s zawierającą te spośród znaków łańcucha str, które są literami
   # albo cyframi (funkcja isalnum), inne znaki (białe, interpunkcyjne) nie powinny
   # bowiem być brane pod uwagę przy badaniu, czy wyrażenie jest palindromem.
   # Zastępujemy ponadto duże litery małymi (funkcja casefold), ponieważ wielkość
   # liter również nie powinna mieć znaczenia.

   s = [c.casefold() for c in str if c.isalnum()]

   # Łańcuch str jest palindromem, gdy w wyniku odwrócenia kolejności elementów
   # listy s otrzymamy wyjściową listę.

   return s == s[::-1]


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

# Przeglądamy kolejno elementy listy argumentów wywołania programu, w przypadku każdego
# z nich sprawdzając, czy jest palindromem, i wypisując go wówczas na standardowe wyjście.

for arg in sys.argv[1:]:
    if is_palindrome(arg):
        print(arg)