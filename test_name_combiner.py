import unittest
from name_combiner import combine_names

class TestNameCombiner(unittest.TestCase):
    def test_empty_names(self):
        self.assertEqual(combine_names("", ""), "")

    def test_single_name(self):
        self.assertEqual(combine_names("Cher", ""), "Cher")
    
    def test_full_name(self):
        self.assertEqual(combine_names("Andrew" ,"Doser"), "Andrew Doser")

if __name__ == '__main__':
    unittest.main()