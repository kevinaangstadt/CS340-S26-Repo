import unittest
from leap_year_check import is_leap_year

class TestLeapYear(unittest.TestCase):
    def test_simple_leap_year(self):
        self.assertTrue(is_leap_year(2024))

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(2023))

    def test_century_non_leap_year(self):
        self.assertFalse(is_leap_year(1900))

if __name__ == '__main__':
    unittest.main()