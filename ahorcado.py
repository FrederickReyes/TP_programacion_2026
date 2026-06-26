import random
import json
import os
from usuarios import guardar_partida

ARCHIVO_PALABRAS = os.path.join(os.path.dirname(__file__), "palabras.json")


def cargar_palabras():
    """
    Carga la lista de palabras (lista de diccionarios) desde el
    archivo palabras.json.

    No recibe parámetros.

    Devuelve una lista de diccionarios, cada uno con la clave "palabra".
    """

    with open(ARCHIVO_PALABRAS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def elegir_palabra_nueva(palabras, palabras_usadas):
    """
    Elige una palabra al azar de la lista de palabras que todavía
    no haya sido usada en la partida actual. Si ya se usaron todas,
    permite que se repitan.

    Parámetros:
        palabras (list): lista de diccionarios con clave "palabra".
        palabras_usadas (list): palabras ya jugadas en esta partida.

    Devuelve un string con la palabra elegida.
    """

    disponibles = []

    for palabra_dict in palabras:

        if palabra_dict["palabra"] not in palabras_usadas:
            disponibles.append(palabra_dict["palabra"])

    if len(disponibles) == 0:

        disponibles = []

        for palabra_dict in palabras:
            disponibles.append(palabra_dict["palabra"])

    return random.choice(disponibles)


def jugar_ahorcado(usuario):
    """
    Juego del Ahorcado. El jugador cuenta con 6 vidas en total y
    debe ir adivinando palabras una tras otra (elegidas al azar,
    sin repetirse hasta agotar el listado). Cada palabra acertada
    suma puntaje y NO recupera vidas; el juego continúa con una
    palabra nueva hasta que se agoten las vidas o el jugador
    decida abandonar ingresando "salir".

    Parámetro: usuario (string) con el nombre del jugador que está
    jugando, para poder guardarle el puntaje obtenido.

    Devuelve el puntaje total acumulado en la partida (int).
    """

    palabras = cargar_palabras()
    palabras_usadas = []

    vidas = 6
    puntaje_total = 0
    palabras_acertadas = 0

    juego_abandonado = False

    print("""
    🪢══════════════════════════════🪢
              🎯 AHORCADO 🎯
    ❤️ Tenés 6 vidas en total
    🔁 Cada palabra que adivines, viene otra nueva
    🚪 Escribí "salir" para abandonar
    🪢══════════════════════════════🪢
    """)

    while vidas > 0 and juego_abandonado == False:

        palabra = elegir_palabra_nueva(palabras, palabras_usadas)
        palabras_usadas.append(palabra)

        letras_adivinadas = []
        letras_usadas = []

        letras_distintas = []

        for letra_de_la_palabra in palabra:

            if letra_de_la_palabra not in letras_distintas:
                letras_distintas.append(letra_de_la_palabra)

        cantidad_pistas = 1

        if cantidad_pistas > len(letras_distintas) - 1:
            cantidad_pistas = len(letras_distintas) - 1

        if cantidad_pistas > 0:

            pistas = random.sample(letras_distintas, cantidad_pistas)

            for pista in pistas:
                letras_adivinadas.append(pista)
                letras_usadas.append(pista)

        palabra_ganada = False

        print(f"\n🆕 Nueva palabra | ❤️ Vidas: {vidas} | ⭐ Puntaje: {puntaje_total}")

        while vidas > 0 and palabra_ganada == False and juego_abandonado == False:

            palabra_mostrada = ""

            for letra_de_la_palabra in palabra:

                if letra_de_la_palabra in letras_adivinadas:
                    palabra_mostrada = palabra_mostrada + letra_de_la_palabra
                else:
                    palabra_mostrada = palabra_mostrada + "_"

            print("\n📝 Palabra:", palabra_mostrada)
            print("❤️ Vidas restantes:", vidas)

            letra = input("🔤 Ingrese una letra (o 'salir'): ").lower()

            if letra == "salir":

                juego_abandonado = True
                print("\n🚪 Abandonaste la partida.")
                print("📖 La palabra era:", palabra)

            elif len(letra) != 1:

                print("⚠️ Debe ingresar una sola letra.")

            elif letra in letras_usadas:

                print("🔄 Ya probaste esa letra. ¡Intentá con otra!")

            else:

                letras_usadas.append(letra)

                if letra in palabra:

                    letras_adivinadas.append(letra)
                    print("✅ ¡Letra correcta!")

                    palabra_completa = True

                    for letra_de_la_palabra in palabra:

                        if letra_de_la_palabra not in letras_adivinadas:
                            palabra_completa = False

                    if palabra_completa == True:
                        palabra_ganada = True

                else:

                    vidas -= 1
                    print("❌ Letra incorrecta. Perdiste una vida 💔")

        if palabra_ganada == True:

            palabras_acertadas += 1
            puntaje_total += vidas

            print(f"\n🎉 ¡Adivinaste! La palabra era: {palabra} 🏆")
            print(f"⭐ Puntaje acumulado: {puntaje_total} pts")

    if juego_abandonado == False:

        print("\n💀 ¡Te quedaste sin vidas! Fin del juego.")

    print(f"\n📊 Resumen: {palabras_acertadas} palabra(s) acertada(s) | "
          f"⭐ Puntaje final: {puntaje_total} pts")

    guardar_partida(usuario, "ahorcado", puntaje_total)

    return puntaje_total
