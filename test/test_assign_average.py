import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        actual = assign_average.switch_average('A')
        self.assertEqual(actual, 90)

    def test_b(self):
        actual = assign_average.switch_average('B')
        self.assertEqual(actual, 80)

    def test_c(self):
        actual = assign_average.switch_average('C')
        self.assertEqual(actual, 70)

    def test_d(self):
        actual = assign_average.switch_average('D')
        self.assertEqual(actual, 60)

    def test_d(self):
        actual = assign_average.switch_average('F')
        self.assertEqual(actual, 50)

    def test_invalid(self):
        actual = assign_average.switch_average('X')
        self.assertEqual(actual, 'Invalid grade')


if __name__ == '__main__':
    unittest.main()
