import random
from palabras import palabras_ahorcado
from usuarios import usuarios


def jugar_ahorcado(usuario):
    """
    Juego del Ahorcado. Elige una palabra al azar de la lista
    palabras_ahorcado, revela 2 letras de pista al empezar, y le
    da al jugador 6 intentos para adivinar el resto de las letras.

    Parámetro: usuario (string) con el nombre del jugador que está
    jugando, para poder sumarle puntaje si gana.

    No devuelve nada, solo imprime el desarrollo del juego y
    actualiza el puntaje del usuario dentro del diccionario usuarios.
    """

    palabra = random.choice(palabras_ahorcado)

    intentos = 6

    # Letras que el jugador ya adivinó bien.
    letras_adivinadas = []

    # Letras que el jugador ya probó (bien o mal), para no dejarlo repetir.
    letras_usadas = []

    # Damos 2 pistas iniciales: revelamos 2 letras distintas de la
    # palabra al azar, como en el ahorcado de mesa.
    letras_distintas = []

    for letra_de_la_palabra in palabra:

        if letra_de_la_palabra not in letras_distintas:

            letras_distintas.append(letra_de_la_palabra)

    cantidad_pistas = 2

    if cantidad_pistas > len(letras_distintas) - 1:

        cantidad_pistas = len(letras_distintas) - 1

    pistas = random.sample(letras_distintas, cantidad_pistas)

    for pista in pistas:

        letras_adivinadas.append(pista)
        letras_usadas.append(pista)

    juego_ganado = False

    print("\n-- AHORCADO --")

    while intentos > 0 and juego_ganado == False:

        # Armamos la palabra para mostrar, letra por letra.
        palabra_mostrada = ""

        for letra_de_la_palabra in palabra:

            if letra_de_la_palabra in letras_adivinadas:

                palabra_mostrada = palabra_mostrada + letra_de_la_palabra

            else:

                palabra_mostrada = palabra_mostrada + "_"

        print("\nPalabra:", palabra_mostrada)
        print("Intentos restantes:", intentos)

        letra = input("Ingrese una letra: ").lower()

        if len(letra) != 1:

            print("Debe ingresar una sola letra.")

        elif letra in letras_usadas:

            print("Ya probó esa letra, intente con otra.")

        else:

            letras_usadas.append(letra)

            if letra in palabra:

                letras_adivinadas.append(letra)

                # Revisamos si ya están todas las letras de la palabra.
                palabra_completa = True

                for letra_de_la_palabra in palabra:

                    if letra_de_la_palabra not in letras_adivinadas:

                        palabra_completa = False

                if palabra_completa == True:

                    juego_ganado = True

            else:

                intentos -= 1
                print("Letra incorrecta.")

    if juego_ganado == True:

        print("\nGanaste! La palabra era:", palabra)
        usuarios[usuario]["puntaje"] += 1

    else:

        print("\nPerdiste.")
        print("La palabra era:", palabra)
