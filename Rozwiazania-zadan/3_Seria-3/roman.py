# Programowanie I R
# Zadania - seria 3.
# Zadanie 3.

import sys


#***********************************************************************************
# Funkcje pomocnicze
#***********************************************************************************

# Zamiana cyfr arabskich na rzymskie
def ToRoman(n):
   num  = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
   res = ""
   while n > 0:
      for i, r in num:
         while n >= i:
            res += r
            n -= i
   return res

# Zamiana cyfr rzymskich na arabskie
def FromRoman(n):
    num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i, c in enumerate(n):
        if (i+1) == len(n) or num[c] >= num[n[i+1]]:
            res += num[c]
        else:
            res -= num[c]
    return res


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

if len(sys.argv) != 3:
   print("Błąd! Niepoprawna liczba argumentów.")
   quit()

if sys.argv[1] == "r": print(ToRoman(int(sys.argv[2])))
elif sys.argv[1] == "a": print(FromRoman(sys.argv[2]))
else: print("Błąd! Nieprawidłowe argumenty.")