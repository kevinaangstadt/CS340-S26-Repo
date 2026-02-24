import unittest
from even_filter import get_evens

class TestEvenFilter(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_evens([]), [])

    def test_odds_and_evens(self):
        self.assertEqual(get_evens([1, 2, 3, 4]), [2, 4])    

if __name__ == '__main__':
    unittest.main()
    
