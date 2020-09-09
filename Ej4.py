import time
# En el programa se comparan dos strings, previamente elegidos de forma
# arbitraria por el programador.


def func_comparación(string_a, string_b):
    print("Buenas noches. Hoy en comparación de cadenas: ")
    time.sleep(1)
    print("Las cadenas a comparar son", '"', string_a, '"', "y", '"',
          string_b, '"')
    time.sleep(3)
    for i in reversed(range(5)):
        print("La gran sorpresa se revelará en", i)
        time.sleep(1)
    # Muestra cuales son los strings a comparar.
    if string_a == string_b:
        # Se comparan ambas strings, en caso de que sean diferentes
        # inefectiblemente una no puede ser la versión capitalizada
        # de la otra.
        print("¡Aleluya!")
        return True
    else:
        # Si se encuentran como diferentes, devuelve un False y le
        # indica al usuario que son diferentes.
        print("La comparación derivó en que ambos strings son",
              "completamente diferentes.")
        return False

if __name__ == "__main__":
    string_a = "Hola, querido Fede."  # Primer string definido.
    string_b = "Deberías elegir mejor los enunciados."
    # Segundo string definido.
    func_comparación(string_a, string_b)
