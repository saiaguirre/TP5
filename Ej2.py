# Este programa cuenta la cantidad de letras "A" encontradas y las compara con
# la cantidad de letras "E" en la misma cadena, y en caso de que sean iguales,
# tanto por tener la misma cantidad como por la inexistencia de ambas, se le
# informa al usuario.


def func_AE():
    # Recibe la cadena por parte del usuario, que va a ser analizada en la
    # función "func_logica()". Esta función solo sirve para que el código
    # quede más ordenado y pueda ser testeable la ya nombrada función.
    AE = input("Por favor, ingrese la cadena de caracteres deseada: ")
    # Cualquier cosa ingresada por el usuario, incluso una sucesión numérica o
    # una cadena vacía es tomado como una cadena válida, simplemente
    # comprobando la existencia o no de las vocales A y/o E en ella.
    func_logica(AE)


def func_logica(AE):
    _ = 0  # Contador
    cant_a = 0  # Si hay una A, se suma a esta variable
    cant_e = 0  # Si hay una E, se suma a esta variable
    lista_string = list(AE)
    for _ in range(len(lista_string)):
        if(lista_string[_] == "A" or lista_string[_] == "a" or
           lista_string[_] == "á" or lista_string[_] == "Á"):
           # En caso de encontrar una A, suma 1 en su debida variable.
            cant_a += 1
        if(lista_string[_] == "E" or lista_string[_] == "e" or
           lista_string[_] == "é" or lista_string[_] == "É"):
            # En caso de encontrar una E, suma 1 en su debida variable.
            cant_e += 1
    if cant_a != 0 or cant_e != 0:
        # Todos los If's anidados a éste solo aplican si en la cadena se
        # registran por lo menos una A o una E.
        if cant_a == cant_e:
            # En caso de que ambas letras aparezcan la misma cantidad de veces.
            print("En la cadena ingresada fueron registradas la misma",
                  "cantidad de letras 'A' y letras 'E' ")
            return "Hay igual cantidad de A's que de E's"
        if cant_a > cant_e:
            # En caso de que la letra A haya sido ingresada más veces.
            print("En la cadena ingresada hay más letras 'A' registradas que",
                  "letras 'E' ")
            return "Hay más A's"
        if cant_e > cant_a:
            # En caso de que la letra E haya sido ingresada más veces.
            print("En la cadena ingresada hay más letras 'E' registradas que",
                  "letras 'A' ")
            return "Hay más E's"
    elif cant_a == 0 and cant_e == 0:
        # En contraste con el If anterior, éste aplica si en la cadena no se
        # ingresa ninguna A o ninguna E.
        print("En la cadena ingresada no se registró ninguna letra 'A' y",
              "ninguna letra 'E' ")
        return "No se encontraron A's o E's"

if __name__ == "__main__":
    func_AE()
