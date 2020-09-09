import unittest
import Ej2


class Tests_Ej2(unittest.TestCase):
    def test_funcionamiento(self):
        # Comprueba el funcionamiento del programa en diferentes casos:
        # En caso de que sean más A's.
        self.assertEquals(Ej2.func_logica("Hola"), "Hay más A's")
        # En caso de que sean más E's.
        self.assertEquals(Ej2.func_logica("Elefante"), "Hay más E's")
        # En caso de que ambos aparezcan la misma cantidad de veces.
        self.assertEqual(Ej2.func_logica("AaEé"), "Hay igual cantidad de A's",
                                                  "que de E's")
        # En caso de que no se encuentre ninguna A o E.
        self.assertEqual(Ej2.func_logica("12345"), "No se encontraron A's o",
                                                   "E's")
        # Teniendo en cuenta lo estricto de la funcionalidad del programa, no
        # se plantean situaciones problemáticas y se centra de forma total en
        # la cantidad de letras 'A' y letras 'E' que puedan encontrarse,
        # permitiendo cadenas numéricas o vacías y encontrándolas válidas.
