# Este programa cuenta la cantidad de veces que aparece cada una de las vocales
# en una cadena. Igual que en ejercicios anteriores, cualquier tipo de cadena
# es permitido, incluidas cadenas vacías y solo numéricas, para responder de
# forma puntual a la consigna.


def vocales(cadena):
    vocs = {"A": 0, "E": 0, "I": 0, "O": 0, "U": 0}
    # Crea el diccionario que asigna una cantidad de veces a cada vocal.
    A = ("a", "A", "á", "Á")
    E = ("e", "E", "é", "É")
    I = ("i", "I", "í", "Í")
    O = ("o", "O", "ó", "Ó")
    U = ("u", "U", "ú", "Ú")
    # Creación de las listas desde la "A" hasta la "U" con todas sus posibles
    # variaciones, para que todas estas sean tomadas en cuenta.
    for letra in cadena:
        for i in range(4):
            if letra == A[i]:
                vocs["A"] = vocs["A"] + 1  # Contador de "A's"
            elif letra == E[i]:
                vocs["E"] = vocs["E"] + 1  # Contador de "E's"
            elif letra == I[i]:
                vocs["I"] = vocs["I"] + 1  # Contador de "I's"
            elif letra == O[i]:
                vocs["O"] = vocs["O"] + 1  # Contador de "O's"
            elif letra == U[i]:
                vocs["U"] = vocs["U"] + 1  # Contador de "U's"
    print("Utilizó " + str(vocs["A"]) + " veces la letra A")
    print("Utilizó " + str(vocs["E"]) + " veces la letra E")
    print("Utilizó " + str(vocs["I"]) + " veces la letra I")
    print("Utilizó " + str(vocs["O"]) + " veces la letra O")
    print("Utilizó " + str(vocs["U"]) + " veces la letra U")
    # Muestra al usuario la cantidad de veces que cada vocal fue usada
    # individualmente.
    vocals = (vocs["A"], vocs["E"], vocs["I"], vocs["O"], vocs["U"])
    # Se crea una lista que contenga la cantidad de veces de uso de las vocales
    # para poder devolverlos y que los tests puedan ser realizables.
    return(vocals)

if __name__ == "__main__":
    cadena = input("Ingrese una cadena de texto: ")
    vocales(cadena)
