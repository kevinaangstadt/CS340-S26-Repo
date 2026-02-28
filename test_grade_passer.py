import unittest
from grade_passer import is_passing

class TestGradePasser(unittest.TestCase):
    def test_high_score(self):
        self.assertTrue(is_passing(95))

    def test_failing_score(self):
        self.assertFalse(is_passing(40))

    #Test case for the reported bug of a score of 60 being considered failing when it should pass
    def test_bug_score(self):
        self.assertTrue(is_passing(60))

if __name__ == '__main__':
    unittest.main()