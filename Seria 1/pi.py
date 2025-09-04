import sys, math
import matplotlib.pyplot as plt

def PI(K):
    Pi=0
    sgn=1
    for n in range(1, 2*(K+1), 2):
        Pi+=sgn/n*(4*(1/5)**n-(1/239)**n)
        sgn*=-1
    return(4*Pi)

N=int(sys.argv[1])


X = range(1,N+1)
Y = [PI(K) for K in range(1,N+1)]
π = [math.pi]*(N)

fig, ax = plt.subplots()
ax.plot(X, Y, label='Oszacowanie')
ax.plot(X, π, label='π')
ax.legend()
ax.set_title(f'π≈{Y[N-1]}')
plt.show()
#plt.savefig(f'factorialgraph({N}).pdf')