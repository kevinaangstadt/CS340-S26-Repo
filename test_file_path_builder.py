import unittest
from file_path_builder import build_path

class TestFilePathBuilder(unittest.TestCase):
    def test_path_with_slash(self):
        self.assertEqual(build_path("/home/user/", "doc.txt"), "/home/user/doc.txt")
    
    def test_path_without_slash(self):
        self.assertEqual(build_path("/home/user", "file.txt"), "/home/user/file.txt")

if __name__ == '__main__':
    unittest.main()