import unittest
from factorial_calculator import factorial

class TestFactorialCalculator(unittest.TestCase):
    def test_factorial_zero_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_five(self):
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()