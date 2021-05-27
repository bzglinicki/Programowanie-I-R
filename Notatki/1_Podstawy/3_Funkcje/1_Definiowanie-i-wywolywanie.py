# Programowanie I R
# Funkcje: definiowanie i wywoływanie

# Materiały:
#    https://www.w3schools.com/python/python_functions.asp
#    https://realpython.com/defining-your-own-python-function/

def f():   # definicja funkcji o nazwie "f"
    msg = "Funkcja f()"
    print(msg)

print("*** Wywołanie funkcji f() ***")
print("---> Główny program...")
f()        # wywołanie funkcji "f"
print("---> Główny program...")
print()

# Funkcja pusta
def pusta():
    pass

print("*** Wywołanie funkcji pusta() ***")
print("---> Główny program...")
pusta()
print("---> Główny program...")
print()