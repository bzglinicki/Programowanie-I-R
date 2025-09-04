from fibi import fibi
from fibr import fibr
import sys, time

import matplotlib.pyplot as plt

def testTime(f, n):
    t1=time.perf_counter_ns()
    f(n)
    t2=time.perf_counter_ns()
    return(t2-t1)

N=int(sys.argv[1])

X = range(N)
I = [testTime(fibi, n) for n in range(N)]
R = [testTime(fibr, n) for n in range(N)]

fig, ax = plt.subplots()
ax.plot(X, R, label='Rekurencyjny')
ax.plot(X, I, label='Iteracyjny')
ax.legend()
#plt.show()
plt.savefig(f'fibgraph({N}).pdf')