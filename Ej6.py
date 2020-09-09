# Este programa devuelve tres versiones de la misma cadena y avisa al usuario
# si es no un palíndromo, ingresada por el usuario. Éstas versiones son:
# 1) Sin vocales, 2) Sin consonantes y 3) Con las vocales cambiadas por su
# vocal siguiente, teniendo en cuenta el orden normalizado de éstas.


def func_solo_consonantes(cadena):
    lista_vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U", "á", "é",
                    "í", "ó", "ú", "Á", "É", "I", "Ó", "Ú")
    # Creo lista con todas las posibilidades de las vocales.
    for x in cadena:
        if x in lista_vocales:
            # Si la letra está dentro de la lista, es removida
            cadena = cadena.replace(x, "")
            # Reemplazo a la cadena por su propia versión modificada
    print("La cadena solo con sus consonantes es: ", cadena)
    return cadena


def func_solo_vocales(cadena):
    lista_vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U", "á", "é",
                    "í", "ó", "ú", "Á", "É", "I", "Ó", "Ú")
    # Creo lista con todas las posibilidades de las vocales.
    for x in cadena:
        if x not in lista_vocales:
            # Si la letra no está dentro de la lista, es removida.
            cadena = cadena.replace(x, "")
            # Reemplazo a la cadena por su propia versión modificada
    print("La cadena solamente con vocales es: ", cadena)
    return cadena


def func_siguiente_vocal(cadena):
    lista_vocales = ("a", "e", "i", "o", "u", "a")
    # Creo lista con todas las vocales en minúscula.
    # (no me juzgues profe, no llegaba)
    lista_cadena = list(cadena)
    for x in range(len(cadena)):
        # Que se repita según la cantidad de caracteres en la cadena.
        for h in range(5):
            # Que se repita por la cantidad de items en la lista lista_vocales.
            if lista_cadena[x] == lista_vocales[h]:
                # Si el item x de la cadena es igual al item h de la lista,
                # que se reemplace
                cadena = cadena.replace(lista_cadena[x], lista_vocales[h + 1])
                # Reemplazo a la cadena por su propia versión modificada.
    print("La cadena ingresada, con las vocales reemplazadas por sus",
          "siguientes es: ", cadena)
    return cadena


def func_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    # Convierto la cadena a minúscula y elimino los espacios.
    if cadena == cadena[::-1]:
        # Si la cadena es igual de derecha a izquierda y viceversa, se marca
        # como palíndromo
        print("La cadena es un palíndromo.")
        return True
    else:
        print("La cadena no es un palíndromo.")
        return False


if __name__ == "__main__":
    cadena = input("Por favor, ingrese la oración a modificar: ")
    func_solo_consonantes(cadena)
    func_solo_vocales(cadena)
    func_siguiente_vocal(cadena)
    func_palindromo(cadena)
