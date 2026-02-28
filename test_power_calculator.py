import unittest
from power_calculator import calculate_power

class TestPowerCalculator(unittest.TestCase):
    def test_two_squared(self):
        self.assertEqual(calculate_power(2, 2), 4)

    def test_power_of_one(self):
        self.assertEqual(calculate_power(5, 1), 5)

    def test_power_of_one(self):
        self.assertEqual(calculate_power(3, 3), 27)

if __name__ == '__main__':
    unittest.main()