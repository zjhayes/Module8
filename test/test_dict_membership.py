import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        test_set = {1, 2, 3, 4, 5}
        item_to_search = 5
        self.assertTrue(dict_membership.in_set(test_set, item_to_search))

    def test_in_dict_false(self):
        test_set = {1, 2, 3, 4}
        item_to_search = 5
        self.assertFalse(dict_membership.in_set(test_set, item_to_search))


if __name__ == '__main__':
    unittest.main()
