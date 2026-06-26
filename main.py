from usuarios import usuarios, registrar_jugador, iniciar_sesion
from funciones import menu_admin, menu_jugador


# MENÚ PRINCIPAL

while True:

    print("""
    🎮══════════════════════════════🎮
            MENU PRINCIPAL
    🎮══════════════════════════════🎮

    1️⃣ Registrarse 📝
    2️⃣ Iniciar sesión 🔐
    3️⃣ Salir 🚪
    """)

    opcion = input("➡️ Seleccione una opción: ")

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
        print("👋 Programa finalizado. ¡Gracias por jugar! 🎮")
        break

    else:
        print("❌ Opción inválida. Elegí 1, 2 o 3.")
