#Rozwiązanie poprzez stworzenie grafu (drzewa) o korzeniu w 1
N=int(10e6)
c={}        #Każdemu elementowi ciągu przypisz następny
l={}        #Odległość danego elementu od 1

l[1]=0
c[1]=4

#Uzupełnij drogę od n do 1
def f(n):
    c[n]=3*n+1 if n%2 else n//2     #Oblicza następny wyraz ciągu
    if c[n] not in c:               #Wywołaj f dla następnego wyrazu, jeżeli jeszcze tego nie zrobiono
        f(c[n])
    l[n]=l[c[n]]+1                  #Ustal odległość od 1

#Znajdź wyraz o największej odległości
m=I=0
for i in range(2,N):        #Od 2, bo wykonanie f(1) nadpisuje odległość
    f(i)
    if l[i]>m:
        m=l[i]
        I=i

print(I)

#Długość ciągu (przed 1):
print(m)
#Bonus: wypisuje ciąg
k=I
while(k!=1):
    print(k, end=', ')
    k=c[k]
print(k)