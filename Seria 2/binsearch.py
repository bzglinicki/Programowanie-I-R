#Funkcja działa rekurencyjnie
#Bonus - znajduje pierwsze występienie elementu
def bin_search(N, L, min, max):         # TODO: Dodać edge-case'y (idiotproofing)
    if(min>=max):                       # Warunek zakończenia rekurencji: przedział zawężony do 1 (lub niepoprawne argumenty)
        return max if L[max]==N else -1 # Element znaleziony lub brak elementu
    
    m=(min+max)//2                      #Środek przedziału
    if N<=L[m]:                         #Czy szukany element w lewej połówce?
        return bin_search(N,L,min,m)    #Szukaj w lewej połówce
    else:
        return bin_search(N,L,m+1,max)  #Szukaj w prawej połówce

n=int(input())
l=[int(i) for i in input().split()]
l.sort()

print(bin_search(n, l, 0, len(l)-1))