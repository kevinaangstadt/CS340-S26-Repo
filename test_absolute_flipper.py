import unittest
from absolute_flipper import get_absolute_value

class TestAbsoluteFlipper(unittest.TestCase):
     def test_negative_input(self):
          refer = get_absolute_value(-3)
          self.assertAlmostEqual(refer, 3.0, places=2)
          self.assertIsInstance(refer, float)

     def test_zero_input(self):
          refer = get_absolute_value(0)
          self.assertAlmostEqual(refer, 0.0, places=2)
          self.assertIsInstance(refer, float)

     def test_postive_input(self):
          refer = get_absolute_value(3)
          self.assertAlmostEqual(refer, 3.0, places=2)
          self.assertIsInstance(refer, float)
     
     def test_bad_input(self):
          with self.assertRaises(TypeError):
               get_absolute_value("1")


if __name__ == '__main__':
     unittest.main()
