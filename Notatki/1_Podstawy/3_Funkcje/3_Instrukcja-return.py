# Programowanie I R
# Funkcje: instrukcja "return"

def g():
    print("Funkcja g() po raz pierwszy.")
    return
    # print("Funkcja g() po raz drugi.") - to się nigdy nie wykona!

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


# Zwracanie wartości ***************************************************************

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


# Zwracanie wielu wartości *********************************************************

def xy():
    return 1, 2

x, y = xy()
print(f"x = {x}, y = {y}")

w = xy()
print(f"w = {w}\nTyp w: {type(w)}")
print()