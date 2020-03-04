import unittest
from datetime import datetime, timedelta
from more_fun_with_collections import half_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        birthday = datetime.datetime(2020, 10, 6)
        half_bday = half_birthday.half_birthday(birthday)
        expected = datetime.datetime(2021, 4, 6)
        self.assertEqual(half_bday, expected)


if __name__ == '__main__':
    unittest.main()
