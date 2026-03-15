import unittest
from color_converter import rgb_to_hex

class TestColorConverter(unittest.TestCase):
    def test_white(self):
        self.assertEqual(rgb_to_hex(255, 255, 255), "#ffffff")
    #added three zeros to check for leading zeros
    def test_black(self):
        self.assertEqual(rgb_to_hex(0, 0, 0), "#000000") 

 #added tests   
    #checking if output where r and g are less than 16 includes leading 0s
    def test_rg_16(self):
        self.assertEqual(rgb_to_hex(8, 12, 31), "#080c1f")

    #checking if output where g and b are less than 16 includes leading 0s
    def test_gb_16(self):
        self.assertEqual(rgb_to_hex(31, 15, 8), "#1f0f08")

    #checking if output where r and b are less than 16 includes leading 0s
    def test_rb_16(self):
        self.assertEqual(rgb_to_hex(10, 255, 3), "#0aff03")


    #checking if output where only r is less than 16 includes leading 0s
    def test_r_16(self):
        self.assertEqual(rgb_to_hex(8, 255, 255), "#08ffff")

    #checking if output where only g is less than 16 includes leading 0s
    def test_g_16(self):
        self.assertEqual(rgb_to_hex(255, 3, 255), "#ff03ff")

    #checking if output where only b is less than 16 includes leading 0s
    def test_g_16(self):
        self.assertEqual(rgb_to_hex(255, 255, 10), "#ffff0a")
        


if __name__ == '__main__':
    unittest.main()
