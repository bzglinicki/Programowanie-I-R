def mul(a, b):
    if type(a) not in [int, float]:
        raise TypeError("Pierwszy czynnik musi być liczbą!")
    
    if type(b) not in [int, float]:
        raise TypeError("Drugi czynnik musi być liczbą!")
    
    return a * b