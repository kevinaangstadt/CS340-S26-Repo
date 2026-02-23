import unittest
from circle_area import calculate_area

class TestCircleArea(unittest.TestCase):
    def test_radius_two(self):
        self.assertAlmostEqual(calculate_area(2), 12.56)

    def test_radius_three(self):
         self.assertAlmostEqual(calculate_area(3), 28.26)
if __name__ == '__main__':
    unittest.main()
