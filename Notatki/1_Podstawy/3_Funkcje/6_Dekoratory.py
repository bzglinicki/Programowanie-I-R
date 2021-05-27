# Programowanie I R
# Funkcje: dekoratory

# Dekoratory to funkcje, które przyjmują jako argument funkcję i zwracają inną funkcję.
# Zasadniczym celem ich stosowania jest dodanie do istniejącej funkcji nowych
# funkcjonalności.

def f():
    print("Funkcja f().")

def dec(fun):
    def inner():
        print("Ten napis jest wyświetlany dzięki zastosowaniu dekoratora!")
        fun()
        print("Ten napis jest wyświetlany dzięki zastosowaniu dekoratora!")
    return inner

f()
print()

# Funkcja fdec jest funkcją f udekorowaną za pomocą dekoratora decr:

fdec = dec(f)
fdec()
print()

# Możemy też zastąpić oryginalną funkcję jej udekorowaną wersją:

f = dec(f)
f()
print()

# Istnieje specjalna składnia pozwalająca na zastosowanie dekoratora w definicji funkcji.

@dec
def g():
    print("Funkcja g().")

g()

print()
print("******************************************************")
print()

# Dekoratory funkcji z argumentami *************************************************

def secondArgumentCannotBeZero(fun):
    def inner(a, b):   # Zestaw argumentów musi być identyczny, jak w przypadku
        if b == 0:     # dekorowanej funkcji. Ten dekorator może zastem zostać
            return "Nie można dzielić przez zero!"   # użyty tylko dla funkcji,
        return fun(a, b)   # które przyjmują dwa argumenty.
    return inner

@secondArgumentCannotBeZero
def divide(a, b):
    return a / b

print("Dzielenie 5 przez 2:")
print(divide(5, 2))
print()

print("Dzielenie 9 przez 0:")
print(divide(9, 0))
print()


def works_for_all(func):
    def inner(*args, **kwargs):   # Tak określony dekorator zadziała dla
        print("Mogę udekorować każdą funkcję!")   # każdej funkcji.
        return func(*args, **kwargs)
    return inner

print()
print("******************************************************")
print()


# Stosowanie wielu dekoratorów *****************************************************

def dec1(func):
    def inner(*args, **kwargs):
        print("* Dekorator dec1 - START!")
        func(*args, **kwargs)
        print("* Dekorator dec1 - STOP!")
    return inner


def dec2(func):
    def inner(*args, **kwargs):
        print("*** Dekorator dec2 - START!")
        func(*args, **kwargs)
        print("*** Dekorator dec2 - STOP!")
    return inner

@dec1
@dec2
def message1():   # message1 = dec1(dec2(message1))
    print("---------> Najpierw dec1, potem dec2.")

@dec2
@dec1
def message2():   # message2 = dec2(dec1(message2))
    print("---------> Najpierw dec2, potem dec1.")

message1()
print()

message2()
print()