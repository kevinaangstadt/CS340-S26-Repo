import unittest
from countdown_generator import generate_countdown

class TestCountdownGenerator(unittest.TestCase):
    def test_start_one(self):
        self.assertEqual(generate_countdown(1)[0], 1)

    # This test checks for the last index of the list
    # and checks if the last index is 0
    def test_for_zero(self): 
        self.assertEqual(generate_countdown(5)[-1], 0)
        

if __name__ == '__main__':
    unittest.main()
