# USUARIOS

usuarios = {}

# Usuario administrador por defecto
usuarios["admin"] = {
    "password": "1234",
    "tipo": "admin",
    "puntaje": 0
}


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
