# Programowanie I R
# Funkcje: generatory

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