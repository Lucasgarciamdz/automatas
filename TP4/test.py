import unittest
from turing_machine import Ejercicio_2a
from turing_machine import Ejercicio_2b
from turing_machine import Ejercicio_2c

class test_turing(unittest.TestCase):
    
    def test_a1(self):
        machine = Ejercicio_2a("xyxyxyxyxyyx")
        self.assertTrue(machine.transactions())
    def test_a2(self):
        machine = Ejercicio_2a("yx")
        self.assertFalse(machine.transactions())
    def test_b1(self):
        machine = Ejercicio_2b("acacacac")
        self.assertTrue(machine.transactions())
    def test_b2(self):
        machine = Ejercicio_2b("aaccccccc")
        self.assertFalse(machine.transactions())
    def test_c1(self):
        machine = Ejercicio_2c("abababababba")
        self.assertTrue(machine.transactions())
    def test_c2(self):
        machine = Ejercicio_2c("ab")
        self.assertFalse(machine.transactions())
    
if __name__ == "__main__":
    unittest.main()
