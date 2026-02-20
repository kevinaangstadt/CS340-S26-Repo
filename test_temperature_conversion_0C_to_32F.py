import unittest
from temperature_utils import to_fahrenheit

class TestTemperatureConverter(unittest.TestCase):
    def test_zero_celsius(self):
        # Checks if 0C is correctly converted to 32F.
        # 
        # Note: since this is float conversion, test uses AlmostEqual assertion
        # to make sure that rounding errors are not counted as errors 
        self.assertAlmostEqual(to_fahrenheit(0), 32, delta=1e-9)