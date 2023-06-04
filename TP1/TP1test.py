import unittest

from TP1 import ejercicio3


class test_ejercicio3(unittest.TestCase):
    def test_1(self):
        cadena = "123"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_2(self):
        cadena = "-5317"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_3(self):
        cadena = "0"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_4(self):
        cadena = "123.321"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_5(self):
        cadena = "-123.321"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_6(self):
        cadena = "123e+321"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_7(self):
        cadena = "-123e-321"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_8(self):
        cadena = "123.321e+321"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_9(self):
        cadena = "-123.321e-321"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_10(self):
        cadena = "123.321e321"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_11(self):
        cadena = "123.321e+321"
        self.assertEqual(ejercicio3(cadena), f"La cadena es valida: {cadena}")

    def test_12(self):
        cadena = ".13213"
        self.assertEqual(ejercicio3(cadena), "La cadena es invalida")

    def test_13(self):
        cadena = "123.321e"
        self.assertEqual(ejercicio3(cadena), "La cadena es invalida")

    def test_14(self):
        cadena = "123.321e+"
        self.assertEqual(ejercicio3(cadena), "La cadena es invalida")

    def test_15(self):
        cadena = "123.321e-"
        self.assertEqual(ejercicio3(cadena), "La cadena es invalida")

    def test_16(self):
        cadena = "123."
        self.assertEqual(ejercicio3(cadena), "La cadena es invalida")

    def test_17(self):
        cadena = "123e"
        self.assertEqual(ejercicio3(cadena), "La cadena es invalida")

    def test_18(self):
        cadena = "123e+"
        self.assertEqual(ejercicio3(cadena), "La cadena es invalida")

    def test_19(self):
        cadena = "123e-"
        self.assertEqual(ejercicio3(cadena), "La cadena es invalida")


if __name__ == '__main__':
    unittest.main()
