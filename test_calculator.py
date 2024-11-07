import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    # Subtract
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)

    def test_subtract_zero(self):
        self.assertEqual(self.calc.subtract(2, 0), 2)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-2, -1), -1) 
    
    # multiply
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-2, -1), 2) 

    #divide
    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 1), 2)

    def test_divide_V2(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    # def test_divide_negative(self):
    #     self.assertEqual(self.calc.divide(-10, -2), 5)

    #modulo
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 5), 0)

    def test_modulo_V2(self):
        self.assertEqual(self.calc.modulo(10, 7), 3)

    
if __name__ == '__main__':
    unittest.main()