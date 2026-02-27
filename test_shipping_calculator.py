import unittest
from shipping_calculator import calculate_shipping

class TestShippingCalculator(unittest.TestCase):
    def test_standard_shipping(self):
        self.assertEqual(calculate_shipping(20), 10)

    def test_free_shipping(self):
        self.assertEqual(calculate_shipping(60), 0)

    def test_edge_case_shipping(self):
        self.assertEqual(calculate_shipping(50), 0)


if __name__ == '__main__':
    unittest.main()
