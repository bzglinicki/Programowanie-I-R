def fibi(n):
    a,b=1,1
    for i in range(2,n):
        a,b=a+b,a
    return a