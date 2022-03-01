# Programowanie I R
# Funkcje: argumenty

# Funkcja z trzema argumentami: name, surname, age
def printPersonalData(name, surname, age):
    print(f"Imię i nazwisko: {name} {surname}")
    print(f"Wiek:            {age}")


# Argumenty pozycyjne **************************************************************

print("Argumenty pozycyjne:\n")

printPersonalData("Jan", "Nowak", 25)   # name = "Jan", surname = "Nowak",
print()                                 # age = 25

printPersonalData(25, "Jan", "Nowak")   # name = 25, surname = "Jan",
print()                                 # age = "Nowak"

# BŁĄD: za mało albo za dużo argumentów:
#    printPersonalData("Jan", "Nowak")
#    printPersonalData("Jan", "Nowak", 25, "jan.nowak@example.com")


# Argumenty z kluczem **************************************************************

print("Argumenty z kluczem:\n")

printPersonalData(name = "Jan", surname = "Nowak", age = 25)
print()

printPersonalData(age = 25, name = "Jan", surname = "Nowak")
print()

# BŁĄD: niepoprawne argumenty, za mało albo za dużo argumentów:
#    printPersonalData(name = "Jan", surname = "Nowak", years = 25)
#    printPersonalData(name = "Jan", surname = "Nowak")
#    printPersonalData(name = "Jan", surname = "Nowak", age = 25,
#                      email = "jan.nowak@example.com")


# Mieszanie obu typów argumentów ***************************************************

print("Argumenty mieszane:\n")

printPersonalData("Jan", surname = "Nowak", age = 25)
print()

printPersonalData("Jan", "Nowak", age = 25)
print()

# Wszystkie argumenty przekazywane pozycyjnie muszą pojawić się przed wszystkimi
# argumentami przekazywanymi przez klucz.

# BŁĄD: niepoprawna kolejność argumentów:
#    printPersonalData(name = "Jan", surname = "Nowak", 25)
#    printPersonalData(name = "Jan", "Nowak", age = 25)
#    printPersonalData("Jan", surname = "Nowak", 25)


# Wartości domyślne argumentów *****************************************************

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


# Argumenty są przekazywane "przez wartość" ****************************************

# Oznacza to, że funkcja tworzy na swoje potrzeby lokalne kopie zmiennych
# przekazanych jej jako argumenty, a nie operuje na pierwotnych zmiennych.

print("Przekazywanie przez wartość:\n")

def inc(x):
    x += 1   # x = x + 1

k = 5
inc(k)
print(k)
print()