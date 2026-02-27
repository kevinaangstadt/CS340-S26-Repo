import unittest
from rectangle_geometry import calculate_perimeter

class TestRectangleGeometry(unittest.TestCase):
    def test_zero_dimensions(self):
        self.assertEqual(calculate_perimeter(0, 0), 0)

    def test_nonzero_dimensions(self):
        self.assertEqual(calculate_perimeter(3, 4), 14)

if __name__ == '__main__':
    unittest.main()