# https://www.w3schools.com/python/python_regex.asp

import re

# 1
string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# Wynik: ['12', '89', '34']

# 2

string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'

result = re.split(pattern, string) 
print(result)

# Wynik: ['Twelve:', ' Eighty nine:', '.']

# 3

string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'

# maxsplit = 1
# Cięcie tylko przy pierwszym wystąpieniu
result = re.split(pattern, string, 1) 
print(result)

# Wynik: ['Twelve:', ' Eighty nine:89 Nine:9.']

# 4
# Usuwanie białych znaków

string = 'abc 12\
de 23 \n f45 6'

pattern = '\s+'

replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

# Wynik: abc12de23f456

# 5
# Wyszukiwanie

string = "Python is fun"

match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

# Wynik: pattern found inside the string