f,p=0,1
S=0
i=0
while f<3000000:
    S+=f
    print(i,f,S)
    f,p=2*f+p,f+p
    i+=2
print(S)