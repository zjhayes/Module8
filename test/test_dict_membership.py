import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        test_set = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
        item_to_search = 5
        self.assertTrue(dict_membership.in_dict(test_set, item_to_search))

    def test_in_dict_false(self):
        test_set = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
        item_to_search = 5
        self.assertFalse(dict_membership.in_dict(test_set, item_to_search))


if __name__ == '__main__':
    unittest.main()
