# Programowanie I R
# Programowanie obiektowe: dziedziczenie wielokrotne

class Base:
    def method(self):
        print("Base: method()")
    
    def methodBase(self):
        print("Base: methodBase()")

class Der1(Base):
    def method(self):
        print("Der1: method()")
    
    def methodDer1(self):
        print("Der1: methodDer1()")

class Der2(Der1):
    def method(self):
        print("Der2: method()")
    
    def methodDer2(self):
        print("Der2: methodDer2()")

b = Base()
d1 = Der1()
d2 = Der2()

b.method()
b.methodBase()
print()

d1.method()
d1.methodBase()
d1.methodDer1()
print()

d2.method()
d2.methodBase()
d2.methodDer1()
d2.methodDer2()

print()
print("**************************************************************")
print()

class Base1:
    def method(self):
        print("Base1: method()")
    
    def methodBase1(self):
        print("Base1: methodBase1()")

    def methodBase(self):
        print("Base1: methodBase()")

class Base2:
    def method(self):
        print("Base2: method()")
    
    def methodBase2(self):
        print("Base2: methodBase2()")

    def methodBase(self):
        print("Base2: methodBase()")

class Der(Base1, Base2):
    def method(self):
        print("Der: method()")
    
    def methodDer(self):
        print("Der: methodDer()")

b1 = Base1()
b2 = Base2()
d = Der()

b1.method()
b1.methodBase()
b1.methodBase1()
print()

b2.method()
b2.methodBase()
b2.methodBase2()
print()

d.method()
d.methodBase()
d.methodBase1()
d.methodBase2()
d.methodDer()