import time
# Esta versión del ejercicio 1 responde a la consigna original y los añadidos
# en el punto 1B, y debido a que tiene sus bases en las consignas del punto
# 1A, éste es agregado también. El punto 1A agrega una cantidad limitada de
# intentos al ingreso de la contraseña y el punto 1B agrega un intervalo de
# tiempo creciente entre cada intento.

# El test de este ejercicio no está realizado debido a que todas las funciones
# no relacionadas con el tiempo entre intentos están testeadas en la versión
# del test EJ1AC.


def func_pedido(cant_intentos):
    # Esta función pide al usuario 5 veces que ingrese la contraseña, y en
    # caso de que éste no logre ingresarla correctamente en esas 5
    # instancias, salta un mensaje de error, avisando que los cantidad de
    # intentos ha sido superada.
    if cant_intentos != 0:
        if cant_intentos > 5:
            return "Cantidad de intentos superada"
    else:
        for cant_intentos in range(5):
            # Setea la cantidad de intentos
            contra = input("Ingrese su contraseña: ")
            contra_ingresada = func_contra(contra)
            # La función "func_contra()" devuelve la contraseña. Teniendo
            # en cuenta ese valor, se vuelve a pedir la contraseña o se le
            # avisa al usuario que la ha ingresado correctamente.
            cant_intentos += 1
            # Contador
            time.sleep(cant_intentos)
            if contra_ingresada is True:
                # Si la contraseña ingresada fue correcta, se consigue un True
                # de la otra función, lo que permite identificarlo, dando pie
                # al aviso y al fin del programa.
                print("¡Contraseña correcta! Bienvenidx.")
                quit()
        for i in reversed(range(4)):
            # Si en los 5 intentos permitidos por el programa no se ingresó
            # correctamente la contraseña, pasa a este for, que deja a un
            # pequeño mensajito que espero que te divierta, Fede ;)
            print("Cantidad de intentos superada. La información se",
                  "autodestruirá en", i)
            time.sleep(1)
        print("¡PUM!")


def func_contra(contra):
    # Esta función compara la cadena ingresa por el usuario por una ya seteada
    # desde el código, devolviendo un True en caso de que sea correcta y un
    # False en caso de que no lo sea, con un mensaje advirtiendo que vuelva a
    # intentarlo.
    contraseña_ok = "Esta contraseña es muy complicada"
    if contra == contraseña_ok:
        # Si la contraseña ingresada fue correcta, se consigue un True
        # de la otra función, lo que permite identificarlo, dando pie
        # al aviso y al fin del programa.
        print("¡Contraseña correcta! Bienvenidx.")
        quit()
    else:
        return False

if __name__ == "__main__":
    cant_intentos = 0
    func_pedido(cant_intentos)
