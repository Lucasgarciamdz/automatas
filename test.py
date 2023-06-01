import unittest
from parameterized import parameterized
from TP3 import check


class test_calcula(unittest.TestCase):
    @parameterized.expand(
        [
            ("1 + 2 + 3", True),
            ("5 % 2", True),
            ("3 + 3 + ( 5 % 2 ) - 3", True),
            ("5 2", True),
            ("5 % ", False),
            ("3 + 3 + ( 5 % 2 ) - ", False),
            ("3 + 3 ( 5 % 2 ) - 3", False),
            ("3 + 3 ( 5 % 2 ) - ", False),
        ]
    )
    def test_1(self, expresion, result):
        self.assertEqual(check(expresion), result)


if __name__ == "__main__":
    unittest.main()
