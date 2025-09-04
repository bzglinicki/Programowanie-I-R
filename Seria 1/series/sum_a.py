def sum_a(x0,n):
    S=0
    x=1
    k=1
    for i in range(n+1):
        k*=max(i,1)
        S+=x/k
#        print(x,k,x/k,S)
        x*=x0
    return S