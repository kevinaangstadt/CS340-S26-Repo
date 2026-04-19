import unittest
from temperature_utils import to_fahrenheit

class TestTemperatureConverter(unittest.TestCase):
    def test_zero_celsius(self):
        # Checks if 0C is correctly converted to 32F.
        # 
        # Note: since this is float conversion, test uses AlmostEqual assertion
        # to make sure that rounding errors are not counted as errors 
        self.assertAlmostEqual(to_fahrenheit(0), 32, places=5)
    def test_hundred_celcius(self):
        # Checks if 100C is converted correctly into 212F
        self.assertAlmostEqual(to_fahrenheit(100), 212, places=5)
    def test_negative_forty(self):
        # Checks if -40C is converted correctly into -40F
        self.assertAlmostEqual(to_fahrenheit(-40), -40, places=5)