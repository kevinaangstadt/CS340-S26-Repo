import unittest
from age_classifier import classify_age

class TestAgeClassifier(unittest.TestCase):
    def test_child(self):
        self.assertEqual(classify_age(10), "Child")
    
    def test_mid_teen(self):
        self.assertEqual(classify_age(15), "Teen")

    def test_adult(self):
        self.assertEqual(classify_age(25), "Adult")
    
    def test_nineteen(self):
        self.assertEqual(classify_age(19), "Teen")

if __name__ == '__main__':
    unittest.main()