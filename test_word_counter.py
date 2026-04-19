import unittest
from word_counter import count_words

class TestWordCounter(unittest.TestCase):
    def test_simple_sentence(self):
        self.assertEqual(count_words("Hello world"), 2)

    def test_single_word(self):
        self.assertEqual(count_words("Python"), 1)

    def test_two_space(self):
        self.assertEqual(count_words("Hello  world"), 2)

if __name__ == '__main__':
    unittest.main()