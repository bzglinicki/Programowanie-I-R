# Błąd

#if a > 3

print("ABC")

# Wyjątek

randomList = [2]
for entry in randomList:
    print("The entry is", entry)
    r = 1/int(entry)
    print(r)


print(dir(locals()['__builtins__']))