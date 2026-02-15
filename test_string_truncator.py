import unittest
from string_truncator import truncate_string

class TestStringTruncator(unittest.TestCase):
    def test_long_string(self):
        self.assertEqual(truncate_string("Hello World", 5), "Hello...")

if __name__ == '__main__':
    unittest.main()