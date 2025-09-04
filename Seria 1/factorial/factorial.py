from ifactorial import ifactorial
from rfactorial import rfactorial
import sys, time

n=int(sys.argv[1])

t1=time.perf_counter_ns()
f=ifactorial(n)
t2=time.perf_counter_ns()
print(f, t2-t1)


t1=time.perf_counter_ns()
f=rfactorial(n)
t2=time.perf_counter_ns()
print(f, t2-t1)