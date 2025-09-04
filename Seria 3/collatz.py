k=int(input())

c=k
while(c!=1):                    #Generujemy kolejne wyrazy ciągu do 1
    print(c, end=', ')
    c=3*c+1 if c%2 else c//2
print(c)