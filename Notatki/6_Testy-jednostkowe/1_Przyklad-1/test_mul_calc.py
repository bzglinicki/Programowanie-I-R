from mul_calc import *
import unittest

### -> DOKUMENTACJA:
###    https://docs.python.org/3/library/unittest.html
###
### -> praktyczny przewodnik
###    https://realpython.com/python-testing/

# Uruchamianie testów:
#    Windows:
#       py -m unittest test_mul_calc.py
#    MacOS / Linux:
#       python3 -m unittest test_mul_calc.py

class Test_mul_calc(unittest.TestCase):
    def test_mul_results(self):
        self.assertAlmostEqual(mul(1, 3), 3)
        self.assertAlmostEqual(mul(2.5, 1.3), 3.25)
        self.assertAlmostEqual(mul(0, 0), 0)
        # self.assertAlmostEqual(mul(9, 0), 9)
    
    def test_mul_input(self):
        self.assertRaises(TypeError, mul, "ABC", "XYZ")
        # self.assertRaises(TypeError, mul, 1, 3)

if __name__ == '__main__':
    unittest.main()