# Programowanie I R
# Zadania - seria 3.
# Zadanie 1.

import sys


#***********************************************************************************
# Funkcja IsPalindrome
#***********************************************************************************

def IsPalindrome(str):
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

# Dzielimy argumenty wywołania programu na przełączniki (opts) i inne argumenty (args).
 
opts = [opt for opt in sys.argv[1:] if opt.startswith("-") or opt.startswith("/")]
args = [arg for arg in sys.argv[1:] if not (arg.startswith("-") or arg.startswith("/"))]

# Sprawdzamy, czy wśród przełączników znajduje się któryś z wymienionych w treści
# zadania. W tym celu tworzymy listę optsAll zawierającą interesujące nas przełączniki,
# a następnie sprawdzamy, czy którykolwiek z elementów tej listy znajduje się na liście
# opts. Jeśli tak jest, przypisujemy zmiennej all wartość True, w przeciwnym przypadku
# - wartość False. Zmienna all pełni więc rolę flagi informującej o tym, w jakim trybie
# pracuje program.

optsAll = ["/a", "/all", "-a", "--all"]
if any(x in opts for x in optsAll): all = True
else: all = False

# Przeglądamy kolejno elementy listy argumentów wywołania niebędących przełącznikami,
# w przypadku każdego z nich sprawdzając, czy jest palindromem, i wypisując na ekranie
# odpowiednie informacje w zależności od trybu pracy programu, czyli wartości zmiennej
# all.

for arg in args:
   if IsPalindrome(arg):
      if all:
         print("    palindrom:", arg)
      else:
         print(arg)
   else:
      if all:
         print("nie palindrom:", arg)