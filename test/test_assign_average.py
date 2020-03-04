import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_a(self):
        actual = assign_average.switch_average(90)
        self.assertEqual(actual, 'A')

    def test_b(self):
        actual = assign_average.switch_average(80)
        self.assertEqual(actual, 'B')

    def test_c(self):
        actual = assign_average.switch_average(70)
        self.assertEqual(actual, 'C')

    def test_d(self):
        actual = assign_average.switch_average(60)
        self.assertEqual(actual, 'D')

    def test_d(self):
        actual = assign_average.switch_average(50)
        self.assertEqual(actual, 'F')

    def test_invalid(self):
        with self.assertRaises(ValueError):
            assign_average.switch_average('F')


if __name__ == '__main__':
    unittest.main()
