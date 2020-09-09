import unittest
import Ej4


class TestEj4(unittest.TestCase):
    def test_comparacion(self):
        string_a = "Hola, querido Fede."  # Primer string definido.
        string_b = "Deberías elegir mejor los enunciados."
        # Segundo string definido.
        self.assertEqual(Ej4.func_comparación(string_a, string_b), False)

if(__name__ == "__main__"):
    unittest.main()
