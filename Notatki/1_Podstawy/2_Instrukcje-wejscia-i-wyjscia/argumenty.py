# Programowanie I R
# Argumenty wywołania programu

# Materiały:
#    https://www.geeksforgeeks.org/command-line-arguments-in-python/
#    https://realpython.com/python-command-line-arguments/

import sys

print(f"Nazwa programu: {sys.argv[0]}")
print(f"Argumenty wywołania programu: {len(sys.argv) - 1}")
for arg in sys.argv[1:]:
    print(f"   {arg}")
print()

opts = [opt for opt in sys.argv[1:] if opt.startswith("-") or opt.startswith("/")]
args = [arg for arg in sys.argv[1:] if not (arg.startswith("-") or arg.startswith("/"))]

print(opts)
print(args)