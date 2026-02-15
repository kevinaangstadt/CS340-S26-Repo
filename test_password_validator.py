import unittest
from password_validator import is_valid_password

class TestPasswordValidator(unittest.TestCase):
    def test_strong_password(self):
        self.assertTrue(is_valid_password("securePassword123"))

    def test_weak_password(self):
        self.assertFalse(is_valid_password("abc"))

if __name__ == '__main__':
    unittest.main()