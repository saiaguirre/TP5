import unittest
import Ej1AC
# En este test, así como en el archivo del ejercicio 1 de éste branch,
# están contemplados los puntos 1A y 1C. Modificaciones que agregan,
# respectivamente, cantidad limitada de intentos al ingreso de la
# contraseña y la devolución de un valor booleano (True o False)
# dependiendo de si el usuario ingresó correctamente o no la contraseña.

# En este test y en el Ejercicio 1 en su totalidad, se toma como válida la
# posibilidad de ingresar cualquier cadena, incluso una vacía. Esto se
# decidió teniendo como referencia inicios de sesión de diferentes
# plataformas utilizadas en la cotidinidad.

class Tests_Ej1(unittest.TestCase):

    def test_contra_correcta(self):
        # Test realizado para comprobar un funcionamiento correcto de la
        # función
        self.assertEqual(
            Ej1AC.func_contra("Esta contraseña es muy complicada"), True)

    def test_contra_incorrecta(self):
        # Comprueba que se devuelva un False en caso de ingresar mal la
        # contraseña
        self.assertEqual(Ej1AC.func_contra("Hola"), False)

    def test_cant_intentos(self):
        # Comprueba que salta un error con cualquier valor de cantidad de
        # intentos mayor a 5, significando esto que solo se puede llegar a 5
        # intentos máximo.
        self.assertEqual(Ej1AC.func_pedido(6),
                         "Cantidad de intentos superada")

if __name__ == "__main__":
    unittest.main()
