import unittest
from average_calculator import calculate_average

class TestAverageCalculator(unittest.TestCase):
    def test_average_basic(self):
        self.assertEqual(calculate_average([10, 20, 30]), 20)

    def test_average_floats(self):
        self.assertEqual(calculate_average([1.5, 2.5, 3.5]), 2.5)

    def test_average_empty_list(self):
        self.assertEqual(calculate_average([]), 0)

if __name__ == '__main__':
    unittest.main()