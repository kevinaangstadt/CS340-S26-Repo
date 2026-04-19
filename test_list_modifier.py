import unittest
from list_modifier import remove_item

class TestListModifier(unittest.TestCase):
    def test_remove_single_occurrence(self):
        self.assertEqual(remove_item([1, 2, 3], 2), [1, 3])

    def test_remove_separated_occurrences(self):
        self.assertEqual(remove_item([1, 2, 3, 2, 4], 2), [1, 3, 4])
    
    def test_remove_consecutive_occurrences(self):
        self.assertEqual(remove_item([1, 2, 2, 3], 2), [1, 3])

if __name__ == '__main__':
    unittest.main()