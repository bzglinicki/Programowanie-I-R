# Programowanie I R
# Funkcje

# Materiały:
#    https://www.w3schools.com/python/python_functions.asp
#    https://realpython.com/defining-your-own-python-function/

# *************************************************************
# Definiowanie i wywoływanie funkcji
# *************************************************************

def f():   # definicja funkcji
    msg = "Funkcja f()"
    print(msg)

print("---> Główny program...")
f()        # wywołanie funkcji
print("---> Główny program...")
print()

# Funkcja pusta
def stub():
    pass

print("---> Główny program...")
stub()
print("---> Główny program...")
print()

# *************************************************************
# Argumenty funkcji
# *************************************************************

def printPersonalData(name, surname, age):
    print(f"Imię i nazwisko: {name} {surname}")
    print(f"Wiek:            {age}")

# Argumenty pozycyjne *****************************************

print("Argumenty pozycyjne:\n")

printPersonalData("Jan", "Nowak", 25)   # name = "Jan", surname = "Nowak",
print()                                 # age = 25

printPersonalData(25, "Jan", "Nowak")   # name = 25, surname = "Jan",
print()                                 # age = "Nowak"

# Błąd:
#    printPersonalData("Jan", "Nowak")
#    printPersonalData("Jan", "Nowak", 25, "jan.nowak@example.com")

# Argumenty z kluczem *****************************************

print("Argumenty z kluczem:\n")

printPersonalData(name = "Jan", surname = "Nowak", age = 25)
print()

printPersonalData(age = 25, name = "Jan", surname = "Nowak")
print()

# Błąd:
#    printPersonalData(name = "Jan", surname = "Nowak", years = 25)
#    printPersonalData(name = "Jan", surname = "Nowak")
#    printPersonalData(name = "Jan", surname = "Nowak", age = 25, email = "jan.nowak@example.com")

# Mieszanie obu typów argumentów ******************************

print("Argumenty mieszane:\n")

printPersonalData("Jan", surname = "Nowak", age = 25)
print()

printPersonalData("Jan", "Nowak", age = 25)
print()

# Błąd:
#    printPersonalData(name = "Jan", surname = "Nowak", 25)
#    printPersonalData(name = "Jan", "Nowak", age = 25)
#    printPersonalData("Jan", surname = "Nowak", 25)

# Wartości domyślne argumentów ********************************

def printPersonalDataDef(name = "Bartłomiej", surname = "Kowalski", age = 20):
    print(f"Imię i nazwisko: {name} {surname}")
    print(f"Wiek:            {age}")

print("Argumenty domyślne:\n")

printPersonalDataDef("Jan", "Nowak", 25)
print()

printPersonalDataDef("Jan", "Nowak")
print()

printPersonalDataDef("Jan")
print()

printPersonalDataDef(age = 30)
print()

printPersonalDataDef()
print()

# Argumenty są przekazywane "przez wartość" *******************

# Oznacza to, że funkcja tworzy na swoje potrzeby lokalne kopie zmiennych
# przekazanych jej jako argumenty, a nie operuje na pierwotnych zmiennych.

print("Przekazywanie przez wartość:\n")

def inc(x):
    x += 1   # x = x + 1

k = 5
inc(k)
print(k)
print()

# *************************************************************
# Instrukcja return. Zwracanie wartości
# *************************************************************

def g():
    print("Funkcja g() po raz pierwszy.")
    return
    # print("Funkcja g() po raz drugi.") - to się nie wykona!

print("Instrukcja return:\n")

print("---> Główny program...")
g()
print("---> Główny program...")
print()

# Instrukcję return można wykorzystać do reagowania na niepoprawne
# wartości argumentów.
def h(x):         # Funkcja oczekuje, że 0 <= x <= 100.
    if x < 0:     # Argument niepoprawny, nie rób nic.
        return

    if x > 100:   # Argument niepoprawny, nie rób nic.
        return

    print(x)

h(-3)
h(105)
h(64)
print()

# Zwracanie wartości ******************************************

def message():
    return "Pozdrawiam!"

msg = message()
print(msg)

def mul5(x):
    return 5 * x

print(mul5(2))
print(mul5(5))
print(mul5(1.3))
print()

# Zwracanie wielu wartości ************************************

def xy():
    return 1, 2

x, y = xy()
print(f"x = {x}, y = {y}")

w = xy()
print(f"w = {w}\nTyp w: {type(w)}")
print()

# Instrukcja yield ********************************************

def one_two_three():
    yield 1
    yield 2
    yield 3

print(one_two_three())

gen = one_two_three()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))   - błąd!

print(tuple(one_two_three()))
print(list(one_two_three()))
print(set(one_two_three()))
# print(dict(one_two_three()))   - błąd!

for x in one_two_three():
    print(x)