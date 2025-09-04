from fibi import fibi
from fibr import fibr
import sys, time

n=int(sys.argv[1])

t1=time.perf_counter_ns()
f=fibi(n)
t2=time.perf_counter_ns()
print(f, t2-t1)


t1=time.perf_counter_ns()
f=fibr(n)
t2=time.perf_counter_ns()
print(f, t2-t1)