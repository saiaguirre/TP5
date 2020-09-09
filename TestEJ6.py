import unittest
import Ej6

# Otra vez, se le da completa libertad al usuario sobre la cadena que desee 
# ingresar, no limitandolo con cadenas sólo numéricas ni vacías y respondiendo
# a lo pedido en todos los casos.

class TestEj6(unittest.TestCase):
    def test_solo_consonantes(self):
        self.assertEqual(Ej6.func_solo_consonantes("hola"), "hl")
        # Comprueba el correcto eliminado de vocales en una cadena.
    
    def test_solo_vocales(self):
        self.assertEqual(Ej6.func_solo_vocales("hola"), "oa")
        # Comprueba el correcto eliminado de consonantes en una cadena.

    def test_siguiente_vocal(self):
        self.assertEqual(Ej6.func_siguiente_vocal("hola"), "hule")
    
    def test_palindromo(self):
        self.assertEqual(Ej6.func_palindromo("hola"), False)

if(__name__ == "__main__"):
    unittest.main()
