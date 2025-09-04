import cmath
a=float(input())
b=float(input())
c=float(input())

D=b*b-4*a*c

x1=(-b+cmath.sqrt(D))/(2*a)
x2=(-b-cmath.sqrt(D))/(2*a)
print(x1, x2)
