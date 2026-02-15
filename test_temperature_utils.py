import unittest
from temperature_utils import to_fahrenheit

class TestTemperatureUtils(unittest.TestCase):
    def test_returns_number(self):
        # Basic smoke test to ensure the function runs and returns a float
        result = to_fahrenheit(100)
        self.assertIsInstance(result, float)

if __name__ == '__main__':
    unittest.main()