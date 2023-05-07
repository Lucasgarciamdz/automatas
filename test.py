import unittest

from calcula import calculate_and_check


class test_calcula(unittest.TestCase):
    def test_1(self):
        expresion = "1 + 2 + 3"
        self.assertTrue(calculate_and_check(expresion))

    def test_2(self):
        expresion = "5 % 2"
        self.assertTrue(calculate_and_check(expresion))

    def test_3(self):
        expresion = "3 + 3 + ( 5 % 2 ) - 3"
        self.assertTrue(calculate_and_check(expresion))

    # def test_4(self):
    #     expresion = "5 2"
    #     self.assertFalse(calculate_and_check(expresion))

    # def test_5(self):
    #     expresion = "5 % "
    #     self.assertFalse.assertFalse(calculate_and_check(expresion))

    # def test_6(self):
    #     expresion = "3 + 3 + ( 5 % 2 ) - "
    #     self.assertFalse(calculate_and_check(expresion))

    # def test_7(self):
    #     expresion = "3 + 3 ( 5 % 2 ) - 3"
    #     self.assertFalse(calculate_and_check(expresion))

    # def test_8(self):
    #     expresion = "3 + 3 ( 5 % 2 ) - "
    #     self.assertFalse(calculate_and_check(expresion))


if __name__ == "__main__":
    unittest.main()
