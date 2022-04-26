# Programowanie I R
# Programowanie obiektowe: własności

class Celsius1:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

human = Celsius1()
human.temperature = 37
print(human.temperature)
print(human.to_fahrenheit())
print()

# **********************************************************************************

class Celsius2:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter
    def get_temperature(self):
        return self._temperature

    # setter
    def set_temperature(self, value):
        if value < -273.15:
            print("Temperature below -273 is not possible")
            return
        self._temperature = value
    
human = Celsius2(37)
print(human.get_temperature())
print(human.to_fahrenheit())
human.set_temperature(-300)
print(human.to_fahrenheit())
print()

# **********************************************************************************

# using property class
class Celsius3:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            print("Temperature below -273 is not possible")
            return
        self._temperature = value

    # Własność
    temperature = property(get_temperature, set_temperature)


human = Celsius3(37)
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = 30
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = -300
print()

# Dekorator ************************************************************************

#    property(fget = None, fset = None, fdel = None, doc = None)

# Using @property decorator
class Celsius4:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            print("Temperature below -273 is not possible")
            return
        self._temperature = value


human = Celsius4(37)
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = 30
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = -300