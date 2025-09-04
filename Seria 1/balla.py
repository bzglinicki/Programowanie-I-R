import math
import sys

try:
    R=float(sys.argv[1])  
except IndexError:
#    print(f"ERROR: {repr(sys.exception())}")
    print("Error: no argument given")
    quit()
print(4*math.pi*R**2, 4/3*math.pi*R**3)