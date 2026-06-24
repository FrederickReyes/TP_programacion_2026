from usuarios import usuarios, ver_usuarios, eliminar_usuario, ver_estadisticas
from ahorcado import jugar_ahorcado


def menu_admin(admin):
    """
    Muestra el menú del administrador en un bucle y ejecuta la
    opción que el usuario elija, hasta que decida cerrar sesión.

    Parámetro: admin (string) con el nombre del administrador
    que inició sesión.

    No devuelve nada.
    """

    while True:

        print("""
===== MENU ADMINISTRADOR =====
1. Ver usuarios
2. Eliminar usuario
3. Ver estadísticas
4. Cerrar sesión
        """)

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


def menu_jugador(usuario):
    """
    Muestra el menú del jugador en un bucle y ejecuta la opción
    que el usuario elija, hasta que decida cerrar sesión.

    Parámetro: usuario (string) con el nombre del jugador
    que inició sesión.

    No devuelve nada.
    """

    while True:

        print("""
===== MENU JUGADOR =====
1. Jugar Ahorcado
2. Ver puntaje
3. Cerrar sesión
        """)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar_ahorcado(usuario)

        elif opcion == "2":
            print("Puntaje total:", usuarios[usuario]["puntaje"])

        elif opcion == "3":
            print("Sesión cerrada.")
            break

        else:
            print("Opción inválida.")
