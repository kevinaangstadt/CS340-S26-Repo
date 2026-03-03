import unittest
from inventory_lookup import find_product

class TestInventoryLookup(unittest.TestCase):
    def test_find_middle_item(self):
        items = ["apple", "banana", "cherry"]
        self.assertEqual(find_product(items, "banana"), 1)

    def test_item_not_found(self):
        items = ["apple", "banana", "cherry"]
        self.assertEqual(find_product(items, "date"), -1)
    
    def test_find_first_item(self):
        items = ["apple", "banana", "cherry"]
        self.assertEqual(find_product(items, "apple"), 0)

if __name__ == '__main__':
    unittest.main()