import unittest
from fizzbuzz_utils import get_fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    # test the existing fizzbuzz issue. Returns "FizzBuzz" if divisible by 3 and 5
    def test_fizzbuzz(self):
        self.assertEqual(get_fizzbuzz(15), "FizzBuzz")
        self.assertEqual(get_fizzbuzz(45), "FizzBuzz")
        self.assertEqual(get_fizzbuzz(-45), "FizzBuzz")

    # Returns "Fizz" if divisible by 3.
    def test_fizz(self):
        self.assertEqual(get_fizzbuzz(3), "Fizz")
        self.assertEqual(get_fizzbuzz(9), "Fizz")
        self.assertEqual(get_fizzbuzz(-9), "Fizz")

    # Returns "Buzz" if divisible by 5.
    def test_buzz(self):
        self.assertEqual(get_fizzbuzz(5), "Buzz")
        self.assertEqual(get_fizzbuzz(10), "Buzz")
        self.assertEqual(get_fizzbuzz(-10), "Buzz")

    # Returns the number as a string otherwise.
    def test_number(self):
        self.assertEqual(get_fizzbuzz(2), "2")
        self.assertEqual(get_fizzbuzz(8), "8")
        self.assertEqual(get_fizzbuzz(-11), "-11")

    # test for correct ouput type (string)
    def test_output_type(self):
        self.assertIsInstance(get_fizzbuzz(3), str)
        self.assertIsInstance(get_fizzbuzz(2), str)

    # test for invalid inputs. Must be int
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_fizzbuzz("1")
        with self.assertRaises(TypeError):
            get_fizzbuzz(8.6)
        with self.assertRaises(TypeError):
            get_fizzbuzz(None)

if __name__ == '__main__':
    unittest.main()