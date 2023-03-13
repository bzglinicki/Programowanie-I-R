# Programowanie I R
# Zadania - seria 3.
# Zadanie 2.

import math
import sys


# Krok I: Analiza wstępna argumentów wywołania programu ****************************

# Zgodnie ze specyfikacją z treści zadania, program musi mieć co najmniej jeden
# argument wywołania (łańcuch określający "tryb" jego pracy). Jeśli tak nie
# jest, wypisujemy komunikat i kończymy pracę programu.

if len(sys.argv) < 2:
   print("Niepoprawne wywołanie programu!")
   quit()   # Kończymy pracę programu.

# Jeden z przełączników /e, /expression, -e lub --expression może się znajdować na
# dowolnej pozycji, również na pierwszej. Dla ułatwienia w sytuacji, gdy przełącznik
# z tej grupy jest pierwszym argumentem, przeniesiemy go na koniec listy argumentów.

optsExpr = ["/e", "/expression", "-e", "--expression"]
if sys.argv[1] in optsExpr: sys.argv.append(sys.argv.pop(1))

# Dzięki temu zabiegowi mamy pewność, że pierwszym argumentem wywołania programu jest
# jeden z łańcuchów definiujących "tryb" jego pracy (dodawanie, mnożenie, pomoc).
# Zbadamy teraz, który to łańcuch, i wykonamy odpowiednią akcję.

elif sys.argv[1] == "add":   # Tryb "dodawanie".
   add = True   # Ustawiamy flagę add - będzie to sygnał, że liczby mają zostać dodane.
elif sys.argv[1] == "mul":   # Tryb "mnożenie".
   add = False   # Wartość False zmiennej add sygnalizuje, że liczby mają zostać pomnożone.
else:   # Pierwszy argument wywołania nie jest żadnym z określonych przełączników.
   print("Niepoprawne wywołanie programu!")
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
# Treść zadania nie pozwala na wystąpienie żadnych innych przełączników,
# zajmiemy się więc również sytuacjami, gdy lista opts zawiera więcej
# niż jeden element oraz gdy zawiera ona jeden element, jednak nie jest on żadnym
# z przełączników z listy optsExpr.

if len(opts) > 1:   # Za dużo przełączników.
   print("Niepoprawne wywołanie programu!")
   quit()   # Kończymy pracę programu.
elif len(opts) == 1:   # Jest jeden przełącznik, to dopuszczalne.
   if opts[0] not in optsExpr:   # Niepoprawny przełącznik.
      print("Niepoprawne wywołanie programu!")
      quit()   # Kończymy pracę programu.
   
   # W tym miejscu znajduje się kod, który zostanie wykonany, gdy użytkownik zastosował
   # jeden z dopuszczonych przełączników. Zgodnie z treścią zadania, musimy w takiej
   # sytuacji wypisać obliczane wyrażenie. Tworzymy zatem pusty łańcuch znaków expr
   # i umieszczamy w nim kolejne liczby przekazane jako argumenty programu, rozdzielając
   # je znakiem odpowiedniego działania. Na końcu łańcucha expr umieszczamy znak równości.
   # Po wszystkim wypisujemy łańcuch expr na standardowe wyjście.
   
   expr = ""
   for arg in args:
      expr += arg + (" + " if add else " * ")
   expr = expr[:-2] + "= "
   print(expr, end = "")


# Krok III: Właściwe obliczenia ****************************************************

# Pozostaje nam już tylko obliczyć sumę lub iloczyn (zgodnie z wolą użytkownika)
# przekazanych programowi liczb. Liczby te znajdują się na liście args, są na niej
# jednak przechowywane w postaci łańcuchów znaków. Tworzymy zatem nową listę
# floatArgs i umieszczamy na niej kolejne elementy listy args, poddając je wcześniej
# konwersji na typ float. Zakładamy tu, że użytkownik podał wyłącznie wartości, które
# reprezentują liczby zmiennoprzecinkowe, nie będziemy rozważać sytuacji, w których
# konwersja na typ float jest niemożliwa.

floatArgs = [float(i) for i in args]

# W zależności od wybranego przez użytkownika działania obliczamy teraz i wypisujemy
# sumę lub iloczyn elementów listy floatArgs. Wykorzystujemy do tego wbudowaną funkcję
# sum oraz funkcję prod z modułu math.

if add: print(sum(floatArgs))
else: print(math.prod(floatArgs))