import unittest
from palindrome_checker import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
    
    def test_upper_palindrome(self):
        self.assertTrue(is_palindrome("Bob"))
    
    def test_upper_non_palindrome(self):
        self.assertFalse(is_palindrome("Bobby"))

if __name__ == '__main__':
    unittest.main()