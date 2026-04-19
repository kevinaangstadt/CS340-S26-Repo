import unittest
from vowel_counter import count_vowels

class TestVowelCounter(unittest.TestCase):
    def test_lowercase_vowels(self):
        self.assertEqual(count_vowels("hello world"), 3)

    def test_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_all_vowels(self):
        self.assertEqual(count_vowels("AEIOU"), 5)

if __name__ == '__main__':
    unittest.main()
