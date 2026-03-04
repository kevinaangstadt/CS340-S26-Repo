import unittest
from set_merger import merge_datasets

class TestSetMerger(unittest.TestCase):
    def test_identical_sets(self):
        self.assertEqual(merge_datasets({1, 2}, {1, 2}), {1, 2})

    def test_disjoint_sets(self):
        self.assertEqual(merge_datasets({1, 2}, {3, 4}), {1, 2, 3, 4})

if __name__ == '__main__':
    unittest.main()

