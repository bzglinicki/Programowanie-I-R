import sys

randomList = ["a", 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        print("The reciprocal of", entry, "is", r)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()

print("*************************************************************")

# *****************************************************************

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        print("The reciprocal of", entry, "is", r)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()

# *********************************************************************

try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass

try:
   a = -20
   if a <= 0:
      raise ValueError("That is not a positive number!")
except ValueError as ve:
      print(ve)

try:
    num = 7
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num   # Może wystąpić ZeroDivisionError
    print(reciprocal)

# **************************************************************************

try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
finally:
   f.close()