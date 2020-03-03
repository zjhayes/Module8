import unittest
from more_fun_with_collections import set_membership


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        test_set = {1, 2, 3, 4, 5}
        item_to_check = 5
        self.assertTrue(set_membership.in_set(test_set, item_to_check))


if __name__ == '__main__':
    unittest.main()
