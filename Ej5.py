# Este programa utiliza la cadena ingresada por el usuario para devolver tres
# versiones de la cadena. Éstas son: solo las siglas de la cadena, la versión
# capitalizada de cada palabra y la devolcuión sólamente de las palabras que
# empiecen con A.


def siglas(cadena):
    # Esta función devuelve las siglas de una string ingresada.
    if not isinstance(cadena, str):
        # En caso de que sea una cadena solamente numérica, devuelve un error.
        raise ValueError
    palabras = cadena.split(" ")  # Divide a la cadena por espacios.
    acorte = ""  # Crea una variable donde se almacenará la cadena modificada.
    for palabra in palabras:
        acorte += palabra[0].upper()
    print(acorte)
    return acorte


def mayuscula(cadena):
    # Ésta función devuelve la misma cadena, pero capitalizada por palabra.
    if not isinstance(cadena, str):
        # En caso de que sea una cadena solamente numérica, devuelve un error.
        raise ValueError
    palabras = cadena.split(" ")  # Divide la cadena por espacios
    frase = ""  # Crea una variable donde se almacenará la cadena modificada.
    for palabra in palabras:
        frase += palabra.capitalize() + " "
        # Almacena la cadena con mayúsculas.
    print(frase)
    return frase


def palabras_con_a(cadena):
    vocal = ["a", "A", "Á", "á"]  # Lista con todas las posibles formas de A.
    if not isinstance(cadena, str):
        # En caso de que sea una cadena solamente numérica, devuelve un error.
        raise ValueError
    palabras = cadena.split(" ")  # Divide a la cadena por espacios.
    frase = ""
    ya_usado = False
    for palabra in palabras:
        ya_usado = False
        for letra in palabra:
            if ya_usado is True:
                continue
            for i in range(4):
                if letra == vocal[i]:
                    frase += palabra + " " 
                    # Almacena la cadena con palabras con A.
                    ya_usado = True  # Hace que se siga analizando al función.
    print(frase)
    return frase

if __name__ == "__main__":
    while True:
        cadena = input("Ingrese una cadena de texto: ")
        try:
            siglas(cadena)
            mayuscula(cadena)
            palabras_con_a(cadena)
        except ValueError:
            print("Por favor ingrese caraceres válidos a la cadena")
