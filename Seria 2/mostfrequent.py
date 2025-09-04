#Sortuje listę, następnie zlicza ile razy dany element się powtarza
#Można prościej
def most_frequent(L):
    if not L:
        return
    L.sort()
    L.append(None)      #Żeby sprawdzić dla ostatniego elementu listy (na n-tym elemencie sprawdzamy (n-1)szy)
    p=None              #Poprzedni element
    n=N=0
    m=[]                #Lista elementów których jest najwięcej
    for i in L:
        if(p==i):           #Jeżeli element się powtórzył (wciąż jesteśmy w ciągu takich samych elementów)
            n+=1
        else:               #Jeżeli nowy element:   (czyli ciąg takich samych się skończył)
            if n>N:         #Jeżeli mamy nowy rekord
                N=n         #Ustal nowe maksimum
                m.clear()   #Zrób nową listę
                m.append(p)
            elif n==N:      #Jeżeli tyle samo, ile było jakiegoś innego
                m.append(p) #Dodaj element do istniejące listy
            n=1             #Zresetuj licznik elementów (licząc już obecny do nowego ciągu)

        p=i                 #W następnej iteracji obecny element stanie się poprzednim
    return [(i,N) for i in m]   #Zwróć listę krotek

l=[int(i) for i in input().split()]
# print(l)
print(most_frequent(l))