# Programowanie I R
# Funkcje: funkcje jako obiekty

def message(msg):
    print(f"Wiadomość: {msg}")

message("Wywołanie message().")

new_message = message
new_message("Wywołanie new_message().")
print()


# Funkcja jako wartość argumentu innej funkcji *************************************

def evaluate(f, x):
    return f(x)

def f1(x):
    return 3 * x

def f2(x):
    return x ** 2

y1 = evaluate(f1, 3)
y2 = evaluate(f2, 5)

print(f"f1(3) = {y1}\nf2(5) = {y2}")
print()


# Funkcja jako wartość zwracana przez inną funkcję *********************************

def getFunction():
    print("Funkcja getFunction().")
    def inner():
        print("Funkcja inner().")
    return inner

fun = getFunction()

fun()
fun()
fun()

# UWAGA!
# Istnieje istotna różnica pomiędzy następującymi dwiema instrukcjami:
#    fun = getFunction
#    fun = getFunction()
# Pierwsza z nich przypisuje do zmiennej fun funkcję getFunction - instrukcja fun()
# będzie wówczas wywołaniem funkcji getFunction; druga natomiast przypisuje do
# zmiennej fun wartość zwracaną przez funkcję getFunction - tym razem instrukcja fun()
# będzie wywołaniem funkcji inner.