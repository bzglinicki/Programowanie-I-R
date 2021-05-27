# Programowanie I R
# Funkcje: funkcje lambda

# Składnia:
#    lambda argumenty: wyrażenie

square = lambda x: x ** 2
y = square(3)
print(y)
print()

# Zastosowanie

# Zachowujemy tylko liczby parzyste
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)

# Zastępujemy liczby ich kwadratami
# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x ** 2, my_list))
print(new_list)