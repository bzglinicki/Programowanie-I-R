# Programowanie I R
# Zadania - seria 3.
# Zadanie 2.

import math
import sys


#***********************************************************************************
# Funkcja pomocnicza help:
# wyświetla informacje o poprawnym wywołaniu programu
#***********************************************************************************

def help():
   print("simplecalc - Prosty kalkulator.\n")
   print("Wywołanie: python simplecalc przełącznik liczby")
   print("   przełącznik - jeden z następujących przełączników:")
   print("      /a, /add, -a lub --add - liczby zostaną dodane,")
   print("      /m, /mul, -m lub --mul - liczby zostaną pomnożone,")
   print("      /?, -h lub --help      - zostanie wyświetlona pomoc,")
   print("   liczby - liczby zmiennoprzecinkowe, na których zostanie wykonana operacja.")
   print("Jeśli wśród argumentów wywołania programu znajdzie się też przełącznik /e, /expression, -e lub --expression, oprócz wyniku zostanie wypisane także obliczane wyrażenie.")


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

# Krok I: Analiza wstępna argumentów wywołania programu ****************************

# Zgodnie ze specyfikacją z treści zadania, program musi mieć co najmniej jeden
# argument wywołania (przełącznik określający "tryb" jego pracy). Jeśli tak nie
# jest, wypisujemy komunikat i kończymy pracę programu.

if len(sys.argv) < 2:
   print("Niepoprawne wywołanie programu!\n")
   help()   # Wyświetlamy pomoc.
   quit()   # Kończymy pracę programu.

# Jeden z przełączników /e, /expression, -e lub --expression może się znajdować na
# dowolnej pozycji, również na pierwszej. Dla ułatwienia w sytuacji, gdy przełącznik
# z tej grupy jest pierwszym argumentem, przeniesiemy go na koniec listy argumentów.

expr_opts = ["/e", "/expression", "-e", "--expression"]
if sys.argv[1] in expr_opts: sys.argv.append(sys.argv.pop(1))

# Dzięki temu zabiegowi mamy pewność, że pierwszym argumentem wywołania programu jest
# jeden z przełączników definiujących "tryb" jego pracy (dodawanie, mnożenie, pomoc).
# Zbadamy teraz, który to przełącznik, i wykonamy odpowiednią akcję.

add_opts = ["/a", "/add", "-a", "--add"]
mul_opts = ["/m", "/mul", "-m", "--mul"]
help_opts = ["/?", "-h", "--help"]

if sys.argv[1] in help_opts:    # Tryb "pomoc".
   help()   # Wyświetlamy pomoc.
   quit()   # Kończymy pracę programu.
elif sys.argv[1] in add_opts:   # Tryb "dodawanie".
   add = True   # Ustawiamy flagę add - będzie to sygnał, że liczby mają zostać dodane.
elif sys.argv[1] in mul_opts:   # Tryb "mnożenie".
   add = False   # Wartość False zmiennej add sygnalizuje, że liczby mają zostać pomnożone.
else:   # Pierwszy argument wywołania nie jest żadnym z określonych przełączników.
   print("Niepoprawne wywołanie programu!\n")
   help()   # Wyświetlamy pomoc.
   quit()   # Kończymy pracę programu.

# Pozostałe argumenty są - zgodnie z treścią zadania - liczbami zmiennoprzecinkowymi,
# może się jednak wśród nich dodatkowo znaleźć jeden z przełączników /e, /expression, -e
# lub --expression. Podzielimy zatem argumenty wywołania programu począwszy od drugiego
# na przełączniki (opts) i inne argumenty (args), by ułatwić dalszą analizę.
 
opts = [opt for opt in sys.argv[2:] if opt.startswith("-") or opt.startswith("/")]
args = [arg for arg in sys.argv[2:] if not (arg.startswith("-") or arg.startswith("/"))]


# Krok II: Obsługa przełącznika e(xpression) ***************************************

# Sprawdzimy teraz, czy wśród przełączników znajduje się /e, /expression, -e
# lub --expression, i - jeśli tak - wypiszemy wyrażenie, którego wartość obliczamy.
# Treść zadania nie pozwala na wystąpienie żadnych innych przełączników oraz domaga
# się wyświetlenia komunikatu pomocy, gdy użytkownik wywoła program z niewłaściwymi
# argumentami, zajmiemy się więc również sytuacjami, gdy lista opts zawiera więcej
# niż jeden element oraz gdy zawiera ona jeden element, jednak nie jest on żadnym
# z przełączników z listy expr_opts.

if len(opts) > 1:   # Za dużo przełączników.
   print("Niepoprawne wywołanie programu!\n")
   help()   # Wyświetlamy pomoc.
   quit()   # Kończymy pracę programu.
elif len(opts) == 1:   # Jest jeden przełącznik, to dopuszczalne.
   if opts[0] not in expr_opts:   # Niepoprawny przełącznik.
      print("Niepoprawne wywołanie programu!\n")
      help()   # Wyświetlamy pomoc.
      quit()   # Kończymy pracę programu.
   
   # W tym miejscu znajduje się kod, który zostanie wykonany, gdy użytkownik zastosował
   # jeden z dopuszczonych przełączników. Zgodnie z treścią zadania, musimy w takiej
   # sytuacji wypisać obliczane wyrażenie. Tworzymy zatem pusty łańcuch znaków expr
   # i umieszczamy w nim kolejne liczby przekazane jako argumenty programu, rozdzielając
   # je znakiem odpowiedniego działania. Na końcu łańcucha expr umieszczamy znak równości.
   # Po wszystkim wypisujemy łańcuch expr na ekranie.
   
   expr = ""
   for arg in args:
      expr += arg + (" + " if add else " * ")
   expr = expr[:-2] + "= "
   print(expr, end = "")


# Krok III: Właściwe obliczenia ****************************************************

# Pozostaje nam już tylko obliczyć sumę lub iloczyn (zgodnie z wolą użytkownika)
# przekazanych programowi liczb. Liczby te znajdują się na liście args, są na niej
# jednak przechowywane w postaci łańcuchów znaków. Tworzymy zatem nową listę
# args_float i umieszczamy na niej kolejne elementy listy args, poddając je wcześniej
# konwersji na typ float. Zakładamy tu, że użytkownik podał wyłącznie wartości, które
# reprezentują liczby zmiennoprzecinkowe, nie będziemy rozważać sytuacji, w których
# konwersja na typ float jest niemożliwa.

args_float = [float(i) for i in args]

# W zależności od wybranego przez użytkownika działania obliczamy teraz i wypisujemy
# sumę lub iloczyn elementów listy args_float. Wykorzystujemy do tego wbudowaną funkcję
# sum oraz funkcję prod z modułu math.

if add: print(sum(args_float))
else: print(math.prod(args_float))