import unittest
from celsius_converter import convert_to_fahrenheit

class TestCelsiusConverter(unittest.TestCase):
    def test_freezing_point(self):
	# Improvement: Using assertAlmostEqual with places=2 to handle 
	# float precision
        self.assertAlmostEqual(convert_to_fahrenheit(0), 32, places=2)

    def test_boiling_point(self):
        # 100 Celsius should be 212 Fahrenheit with places=2 to handle
	# float precision
        self.assertAlmostEqual(convert_to_fahrenheit(100), 212, places=2)

if __name__ == '__main__':
    unittest.main()
