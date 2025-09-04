def sum_b(x0,n):
    S=0
    x=1
    k=1
    sgn=1
    for i in range(n+1):
        S+=sgn*x*x/k
#        print(x,k,x/k,S)
        k*=(2*i+1)*(2*i+2)
        x*=x0
        sgn*=-1
    return S