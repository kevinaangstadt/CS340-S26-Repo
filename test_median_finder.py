import unittest
from median_finder import find_median

class TestMedianFinder(unittest.TestCase):
    def test_sorted_list(self):
        self.assertEqual(find_median([1, 2, 3]), 2)

    def test_longer_sorted_list(self):
        self.assertEqual(find_median([10, 20, 30, 40, 50]), 30)

    def test_unsorted_list(self):
        self.assertEqual(find_median([3, 1, 2]), 2)

    def test_longer_unsorted_list(self):
        self.assertEqual(find_median([3, 2, 4, 1, 3]), 3)

if __name__ == '__main__':
    unittest.main()
