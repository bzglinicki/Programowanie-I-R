from random import randint as rng

a=set()                 
while(len(a)<6):        #Chcemy zbiór 6-elementowy
    a.add(rng(1,49))

a=list(a)
a.sort()

[print(i, end=" ") for i in a]
print()