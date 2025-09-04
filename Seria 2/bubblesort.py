def bubble_sort(L):
    b=1             #Czy kontynuować sortowanie?
    while(b):
        b=0         #Jeżeli nie będzie trzeba zamienić żadnej pary, ta wartość się nie zmieni 
        for i in range(len(L)-1):
            if(L[i]>L[i+1]):
                L[i],L[i+1]=L[i+1],L[i]     #Zamień miejscami
                b=1

l=[int(i) for i in input().split()]
bubble_sort(l)
print(l)