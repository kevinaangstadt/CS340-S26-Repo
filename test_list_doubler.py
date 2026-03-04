import unittest
from list_doubler import double_elements

class TestListDoubler(unittest.TestCase):
    def test_zero_element(self):
        self.assertEqual(double_elements([]), [])

    def test_correct_double(self):
        self.assertEqual(double_elements([1,2]), [2,4])

if __name__ == '__main__':
    unittest.main()