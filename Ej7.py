def agenda(nombre, personas):
    if not isinstance(nombre, str):
        # Si es una cadena solamente numérica, tira error.
        raise ValueError
    if str.isnumeric(nombre):
        raise ValueError
    if nombre == "*": # Valor centinela de salida del programa
        quit()
    if nombre in personas:
        if True:
            # Si se encuentra el nombre, se muestra éste con su número
            print("El número de " + nombre + " es " + str(personas[nombre]))
            return personas[nombre]
    else:
        # En caso de que no sea encontrado, se agrega un nuevo índice
        nueva_persona(nombre, "", personas)


def nueva_persona(nombre, telefono, personas):
    mensaje = "Por favor ingrese el nuevo número para " + nombre + ": "
    while True:
        nuevo_tel = inputs(mensaje, telefono)
        try: 
            nuevo_tel = int(nuevo_tel)
            # Comprueba que el número de teléfono ingresado no contenga
            # caracteres no numéricos
            personas[nombre] = nuevo_tel
            # Se asocia este teléfono al nombre ingresado
            los_dos = (nombre, personas[nombre])
            # Crea una variable para tener a ambos juntos y poder testearlo.
            return los_dos
            break
        except ValueError:
            print("Ingrese valores númerico para el teléfono")


def inputs(mensaje, var):
    if __name__ == "__main__":
        var = input(mensaje)
        return var
    else:
        return var

if __name__ == "__main__":
    personas = {"Mateo": 4323454231, "Ivan": 4356721312, "Manuel": 4356749876}
    while True:
        nombre = input("Por favor ingrese un nombre: ")
        try:
            agenda(nombre, personas)
        except ValueError:
            print("Por favor ingrese caracteres válidos para el nombre")
