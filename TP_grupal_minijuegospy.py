
# PLATAFORMA DE MINIJUEGOS

import random


# LISTAS Y DATOS


usuarios = {}

# Usuario administrador por defecto
usuarios["admin"] = {
    "password": "1234",
    "tipo": "admin",
    "puntaje": 0
}


# FUNCIONES GENERALES

def registrar_jugador():
    print("\n-- Registro de jugador --")

    usuario = input("Ingrese un nombre de usuario: ")

    if usuario in usuarios:
        print("Ese usuario ya existe.")
        return

    password = input("Ingrese una contraseña: ")

    usuarios[usuario] = {
        "password": password,
        "tipo": "jugador",
        "puntaje": 0
    }

    print("Jugador registrado correctamente.")


def iniciar_sesion():
    print("\n--- INICIAR SESION ---")

    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    if usuario in usuarios and usuarios[usuario]["password"] == password:
        print("Inicio de sesión correcto.")
        return usuario
    else:
        print("Datos incorrectos.")
        return None



# FUNCIONES ADMINISTRADOR

def menu_admin(admin):
    while True:
        print("\n===== MENU ADMINISTRADOR =====")
        print("1. Ver usuarios")
        print("2. Eliminar usuario")
        print("3. Ver estadísticas")
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_usuarios()

        elif opcion == "2":
            eliminar_usuario()

        elif opcion == "3":
            ver_estadisticas()

        elif opcion == "4":
            print("Sesión cerrada.")
            break

        else:
            print("Opción inválida.")


def ver_usuarios():
    print("\n--- LISTA DE USUARIOS ---")

    for usuario, datos in usuarios.items():
        print("Usuario:", usuario)
        print("Tipo:", datos["tipo"])
        print("Puntaje:", datos["puntaje"])
        print("-------------------")


def eliminar_usuario():
    usuario = input("Ingrese el usuario a eliminar: ")

    if usuario == "admin":
        print("No se puede eliminar el administrador.")
        return

    if usuario in usuarios:
        del usuarios[usuario]
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")


def ver_estadisticas():
    print("\n-- ESTADISTICAS --")

    cantidad = len(usuarios)
    print("Cantidad total de usuarios:", cantidad)

    mayor = 0
    mejor_jugador = ""

    for usuario, datos in usuarios.items():

        if datos["tipo"] == "jugador":

            if datos["puntaje"] > mayor:
                mayor = datos["puntaje"]
                mejor_jugador = usuario

    print("Mejor jugador:", mejor_jugador)
    print("Mayor puntaje:", mayor)


# FUNCIONES JUGADOR

def menu_jugador(usuario):
    while True:
        print("\n===== MENU JUGADOR =====")
        print("1. Jugar Piedra Papel o Tijera")
        print("2. Jugar Ahorcado")
        print("3. Ver puntaje")
        print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar_piedra_papel_tijera(usuario)

        elif opcion == "3":
            print("Puntaje total:", usuarios[usuario]["puntaje"])

        elif opcion == "4":
            print("Sesión cerrada.")
            break

        else:
            print("Opción inválida.")



# MINIJUEGO:
# PIEDRA PAPEL O TIJERA


def jugar_piedra_papel_tijera(usuario):

    opciones = ["piedra", "papel", "tijera"]

    print("\n-- PIEDRA PAPEL O TIJERA --")

    jugador = input("Elija piedra, papel o tijera: ").lower()

    if jugador not in opciones:
        print("Opción inválida.")
        return

    computadora = random.choice(opciones)

    print("La computadora eligió:", computadora)

    # Empate
    if jugador == computadora:
        print("Empate.")

    # Casos donde gana el jugador
    elif (
        (jugador == "piedra" and computadora == "tijera") or
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "tijera" and computadora == "papel")
    ):

        print("Ganaste la ronda.")
        usuarios[usuario]["puntaje"] += 1

    else:
        print("Perdiste la ronda.")



# MENU


while True:

    print("\n========== MENU PRINCIPAL ==========")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_jugador()

    elif opcion == "2":

        usuario = iniciar_sesion()

        if usuario is not None:

            tipo = usuarios[usuario]["tipo"]

            if tipo == "admin":
                menu_admin(usuario)

            elif tipo == "jugador":
                menu_jugador(usuario)

    elif opcion == "3":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")