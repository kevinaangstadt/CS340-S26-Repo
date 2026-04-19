import unittest
from bmi_calculator import calculate_bmi

class TestBMICalculator(unittest.TestCase):
    def test_unit_dimensions(self):
        self.assertEqual(calculate_bmi(1, 1), 1)
    def test_bigger_numbers(self):
        #testing with 80kg and 2m
        self.assertEqual(calculate_bmi(80, 2), 20)
        # this checks that the output of the functio calculate_bmi, with 80 and 2 as parameters, is equal to 20


if __name__ == '__main__':
    unittest.main()
