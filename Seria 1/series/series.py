import sum_a, sum_b
import sys
x=0
n=0
try:
    x=float(sys.argv[1])
    n=int(sys.argv[2])
except IndexError:
    print("Error - expected 2 arguments")
    exit()
except ValueError:
    print("Error - wrong input format")
    exit()

print(sum_a.sum_a(x,n), sum_b.sum_b(x,n))