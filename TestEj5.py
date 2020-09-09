import unittest
import Ej5


class TestEj5(unittest.TestCase):
    def test_siglas(self):
        self.assertEquals(Ej5.siglas("Universal Serial Bus"), "USB")
        self.assertEquals(Ej5.siglas("uNiVeRsal SeRiAl bUs"), "USB")
        self.assertEquals(Ej5.siglas("Complete the Monument"), "CTM")
        with self.assertRaises(ValueError):
            Ej5.siglas([0, 3, 4242])

    def test_mayusculas(self):
        self.assertEquals(Ej5.mayuscula("republica argentina"), "Republica" +
                                                                " Argentina ")
        self.assertEquals(Ej5.mayuscula("hOlA coMo eSTas"), "Hola Como Estas ")
        with self.assertRaises(ValueError):
            Ej5.mayuscula(2)

    def test_palabras_con_a(self):
        self.assertEquals(Ej5.palabras_con_a("Buenos dias mamá"), "dias mamá ")
        self.assertEquals(Ej5.palabras_con_a("extraño a avi"), "extraño a avi ")
        self.assertEquals(Ej5.palabras_con_a("Hoy va a volver :)"), "va a ")
        with self.assertRaises(ValueError):
            Ej5.palabras_con_a(35564)

if __name__ == "__main__":
    unittest.main()
