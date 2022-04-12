# Programowanie I R
# Zadania - seria 4.
# Zadanie 2.


#***********************************************************************************
# Klasa Stack
#***********************************************************************************

class Stack:
   def __init__(self):
      self._items = []

   def is_empty(self):
      return not self._items

   def push(self, item):
      if item:
         self._items.append(item)
         return True
      else:
         return False

   def pop(self):
      if self.is_empty():
         return None
      else:
         return self._items.pop()

   def peek(self):
      if self.is_empty():
         return None
      else:
         return self._items[-1]

   def size(self):
      return len(self._items)


#***********************************************************************************
# Główny kod programu
#***********************************************************************************

s = Stack()

for arg in sys.argv[1:]:
    s.push(arg)

while not s.is_empty():
	print(s.pop())