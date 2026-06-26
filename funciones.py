from usuarios import (
    ver_usuarios,
    modificar_usuario,
    eliminar_usuario,
    ver_estadisticas,
    ver_datos_personales,
    ver_puntajes,
)
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

        print(f"""
    👑══════════════════════════════👑
         MENÚ ADMINISTRADOR
         Hola, {admin}!
    👑══════════════════════════════👑

    1️⃣ Ver estadísticas 📊
    2️⃣ Modificar usuario ✏️
    3️⃣ Eliminar usuario 🗑️
    4️⃣ Ver usuarios 👥
    5️⃣ Probar juego (Ahorcado) 🪢
    6️⃣ Cerrar sesión 🚪
        """)

        opcion = input("➡️ Seleccione una opción: ")

        if opcion == "1":
            ver_estadisticas()

        elif opcion == "2":
            modificar_usuario()

        elif opcion == "3":
            eliminar_usuario()

        elif opcion == "4":
            ver_usuarios()

        elif opcion == "5":
            jugar_ahorcado(admin)

        elif opcion == "6":
            print("👋 Sesión cerrada. ¡Hasta pronto! 👑")
            break

        else:
            print("❌ Opción inválida. Elegí del 1 al 6.")


def menu_jugador(usuario):
    """
    Muestra el menú del jugador en un bucle y ejecuta la opción
    que el usuario elija, hasta que decida cerrar sesión.

    Parámetro: usuario (string) con el nombre del jugador
    que inició sesión.

    No devuelve nada.
    """

    while True:

        print(f"""
    🎯══════════════════════════════🎯
           MENÚ JUGADOR
           Hola, {usuario}!
    🎯══════════════════════════════🎯

    1️⃣ Ver datos personales 🪪
    2️⃣ Jugar Ahorcado 🪢
    3️⃣ Ver puntajes 🏆
    4️⃣ Cerrar sesión 🚪
        """)

        opcion = input("➡️ Seleccione una opción: ")

        if opcion == "1":
            ver_datos_personales(usuario)

        elif opcion == "2":
            jugar_ahorcado(usuario)

        elif opcion == "3":
            ver_puntajes(usuario)

        elif opcion == "4":
            print("👋 Sesión cerrada. ¡Nos vemos en la próxima! 🎮")
            break

        else:
            print("❌ Opción inválida. Elegí del 1 al 4.")
