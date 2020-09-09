import unittest
import Ej3
# Acatando la libertad dada al usuario en el Ejercicio 3 y anteriores, no se
# presentan situaciones conflictivas para centrarse de forma total en el
# contado de vocales.


class TestEj3(unittest.TestCase):
    # Comprueba el funcionamiento del programa en diferentes casos, tales
    # como la colocación de mayúsculas o vocales tildadas.
    def test_vocales(self):
        # El orden de las vocales se respeta en la colocación de valores de uso
        # individual. Esto quiere decir que en una cadena "(1, 2, 3, 4, 5)" se
        # representa que fueron colocadas: una "A", dos "E", tres "I", cuatro
        # "O" y cinco "U"
        self.assertEquals(Ej3.vocales("hola"), (1, 0, 0, 1, 0))
        # Testea en caso de que sea completamente minúscula.
        self.assertEquals(Ej3.vocales("hOLa"), (1, 0, 0, 1, 0))
        # En este caso se presenta una "O" mayúscula.
        self.assertEquals(Ej3.vocales("hOlA lunA Cómo estás?"),
                                     (3, 1, 0, 3, 1))
        # En éste se plantea la mezcla entre mayúsculas (ya funcionales) y
        # vocales tildadas.
        self.assertEquals(Ej3.vocales("HOLA MUNDO"), (1, 0, 0, 2, 1))
        # Testea que se tomen en cuenta incluso en strings completamente
        # capitalizadas
        self.assertEquals(Ej3.vocales("'¿'¿'09&%##"), (0, 0, 0, 0, 0))
        # Comprueba el correcto funcionamiento incluso cuando ningún caracter
        # alfabético es ingresado

if __name__ == "__main__":
    unittest.main()
