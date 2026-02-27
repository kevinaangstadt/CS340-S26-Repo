import unittest
from prime_checker import is_prime

class TestPrimeChecker(unittest.TestCase):
    def test_prime_seven(self):
        self.assertTrue(is_prime(7))

    def test_composite_four(self):
        self.assertFalse(is_prime(4))

    def test_composite_one(self):
        self.assertFalse(is_prime(1))

    def test_composite_minus_one(self):
        self.assertFalse(is_prime(-1))

    def test_composite_minus_hundred(self):
        self.assertFalse(is_prime(-100))

    def test_composite_hundred(self):
        self.assertFalse(is_prime(100))

if __name__ == '__main__':
    unittest.main()