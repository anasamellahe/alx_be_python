import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1, 1), 2)
        self.assertEqual(self.calc.add(3, 1), 4)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(3, 1), 2)

    def test_division(self):
        self.assertEqual(self.calc.divide(2, 0), None)
        self.assertEqual(self.calc.divide(1, 1), 1)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(3, 1), 3)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)
        self.assertEqual(self.calc.multiply(1, 1), 1)
        self.assertEqual(self.calc.multiply(10, 2), 20)
        self.assertEqual(self.calc.multiply(4, 9), 36)

if __name__ == "__main__":
    unittest.main()
