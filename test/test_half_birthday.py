import unittest
from datetime import datetime, timedelta
from more_fun_with_collections import half_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime(2020, 10, 6, 0, 0)
        half_bday = half_birthday.half_birthday(birthday)
        expected = datetime(2021, 4, 6, 12, 0)
        self.assertEqual(half_bday, expected)


if __name__ == '__main__':
    unittest.main()
