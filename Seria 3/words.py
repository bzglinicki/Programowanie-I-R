a=input().split()
d={}                #Słownik (słowo, ilość)
a.sort()
for i in a:
    #Jeżeli słowo jest w słowniku, zwiększ liczbę występień o 1,
    # w przeciwnym razie ustal 1
    d[i]=d[i]+1 if i in d else 1

for i in d:
    print(i, d[i])