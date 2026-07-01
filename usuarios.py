import json
import os

# ARCHIVO DE PERSISTENCIA
ARCHIVO_USUARIOS = os.path.join(os.path.dirname(__file__), "usuarios.json")


def cargar_usuarios():
    """
    Carga el diccionario de usuarios desde el archivo usuarios.json.
    Si el archivo no existe, crea uno con el usuario admin por defecto.

    No recibe parámetros.

    Devuelve un diccionario con todos los usuarios registrados.
    """

    if not os.path.exists(ARCHIVO_USUARIOS):

        usuarios_default = {
            "admin": {
                "password": "1234",
                "tipo": "admin",
                "edad": 99,
                "puntajes": []
            }
        }

        guardar_usuarios(usuarios_default)
        return usuarios_default

    with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_usuarios(usuarios_a_guardar):
    """
    Guarda el diccionario de usuarios recibido en el archivo usuarios.json.

    Parámetro: usuarios_a_guardar (dict) con todos los usuarios.

    No devuelve nada.
    """

    with open(ARCHIVO_USUARIOS, "w", encoding="utf-8") as archivo:
        json.dump(usuarios_a_guardar, archivo, indent=4, ensure_ascii=False)


# Diccionario de usuarios cargado en memoria al iniciar el programa
usuarios = cargar_usuarios()


def registrar_jugador():
    """
    Registra un nuevo usuario de tipo jugador, pidiendo nombre,
    contraseña y edad. Guarda los cambios en el archivo JSON.

    No recibe parámetros ni devuelve nada.
    """

    print("\n📝══════════════════════════════📝")
    print("        REGISTRO DE JUGADOR")
    print("📝══════════════════════════════📝")

    usuario = input("👤 Ingrese un nombre de usuario: ")

    if usuario in usuarios:
        print("⚠️ Ese usuario ya existe.")
        return

    password = input("🔑 Ingrese una contraseña: ")

    edad_valida = False
    edad = 0

    while edad_valida == False:

        edad_texto = input("🎂 Ingrese su edad: ")

        if edad_texto.isdigit():
            edad = int(edad_texto)
            edad_valida = True
        else:
            print("⚠️ Ingrese un número válido para la edad.")

    usuarios[usuario] = {
        "password": password,
        "tipo": "jugador",
        "edad": edad,
        "puntajes": []
    }

    guardar_usuarios(usuarios)

    print("✅ Jugador registrado correctamente.")


def iniciar_sesion():
    """
    Pide usuario y contraseña, y valida contra el diccionario
    de usuarios cargado en memoria.

    No recibe parámetros.

    Devuelve el nombre de usuario (string) si las credenciales son
    correctas, o None si son incorrectas.
    """

    print("\n🔐══════════════════════════════🔐")
    print("          INICIAR SESIÓN")
    print("🔐══════════════════════════════🔐")

    usuario = input("👤 Usuario: ")
    password = input("🔑 Contraseña: ")

    if usuario in usuarios and usuarios[usuario]["password"] == password:
        print(f"✅ ¡Bienvenido/a, {usuario}!")
        return usuario
    else:
        print("❌ Usuario o contraseña incorrectos.")
        return None


def ver_datos_personales(usuario):
    """
    Muestra los datos personales del usuario logueado.

    Parámetro: usuario (string) con el nombre del usuario actual.

    No devuelve nada.
    """

    datos = usuarios[usuario]

    print("\n🪪══════════════════════════════🪪")
    print("        DATOS PERSONALES")
    print("🪪══════════════════════════════🪪")
    print(f"👤 Nombre de usuario: {usuario}")
    print(f"🎂 Edad: {datos['edad']}")
    print(f"🎭 Tipo de cuenta: {datos['tipo']}")
    print(f"🏆 Cantidad de partidas jugadas: {len(datos['puntajes'])}")


def ver_usuarios():
    """
    Muestra el listado completo de usuarios registrados, con sus datos.

    No recibe parámetros ni devuelve nada.
    """

    print("\n👥══════════════════════════════👥")
    print("        LISTA DE USUARIOS")
    print("👥══════════════════════════════👥")

    for usuario, datos in usuarios.items():
        print(f"👤 Usuario: {usuario}")
        print(f"🎭 Tipo: {datos['tipo']}")
        print(f"🎂 Edad: {datos['edad']}")
        print(f"🏆 Partidas jugadas: {len(datos['puntajes'])}")
        print("-------------------")


def modificar_usuario():
    """
    Permite al administrador modificar la contraseña o la edad
    de un usuario existente. Guarda los cambios en el JSON.

    No recibe parámetros ni devuelve nada.
    """

    print("\n✏️══════════════════════════════✏️")
    print("        MODIFICAR USUARIO")
    print("✏️══════════════════════════════✏️")

    usuario = input("👤 Ingrese el usuario a modificar: ")

    if usuario not in usuarios:
        print("❌ Usuario no encontrado.")
        return

    print("""
    1️⃣ Cambiar contraseña 🔑
    2️⃣ Cambiar edad 🎂
    3️⃣ Cancelar ❌
    """)

    opcion = input("➡️ Seleccione una opción: ")

    if opcion == "1":

        nueva_password = input("🔑 Ingrese la nueva contraseña: ")
        usuarios[usuario]["password"] = nueva_password
        guardar_usuarios(usuarios)
        print("✅ Contraseña actualizada.")

    elif opcion == "2":

        edad_valida = False

        while edad_valida == False:

            edad_texto = input("🎂 Ingrese la nueva edad: ")

            if edad_texto.isdigit():
                usuarios[usuario]["edad"] = int(edad_texto)
                edad_valida = True
                guardar_usuarios(usuarios)
                print("✅ Edad actualizada.")
            else:
                print("⚠️ Ingrese un número válido.")

    elif opcion == "3":
        print("🚫 Operación cancelada.")

    else:
        print("❌ Opción inválida.")


def eliminar_usuario():
    """
    Elimina un usuario del sistema (excepto el admin) y guarda
    los cambios en el archivo JSON.

    No recibe parámetros ni devuelve nada.
    """

    print("\n🗑️══════════════════════════════🗑️")
    print("        ELIMINAR USUARIO")
    print("🗑️══════════════════════════════🗑️")

    usuario = input("👤 Ingrese el usuario a eliminar: ")

    if usuario == "admin":
        print("⚠️ No se puede eliminar al administrador.")
        return

    if usuario in usuarios:
        del usuarios[usuario]
        guardar_usuarios(usuarios)
        print("✅ Usuario eliminado.")
    else:
        print("❌ Usuario no encontrado.")


def guardar_partida(usuario, juego, puntaje):
    """
    Registra el resultado de una partida jugada por el usuario,
    agregándola a su historial de puntajes, y guarda los cambios
    en el archivo JSON.

    Parámetros:
        usuario (string): nombre del usuario que jugó.
        juego (string): nombre del juego jugado (ej: "ahorcado").
        puntaje (int): puntaje obtenido en la partida.

    No devuelve nada.
    """

    partida = {
        "juego": juego,
        "puntaje": puntaje
    }

    usuarios[usuario]["puntajes"].append(partida)
    guardar_usuarios(usuarios)


def obtener_top_10():
    """
    Recorre todas las partidas de todos los usuarios y devuelve
    las 10 mejores, ordenadas de mayor a menor puntaje.

    No recibe parámetros.

    Devuelve una lista de diccionarios con claves "usuario",
    "juego" y "puntaje", ordenada de mayor a menor.
    """

    todas_las_partidas = []

    for usuario, datos in usuarios.items():

        for partida in datos["puntajes"]:

            todas_las_partidas.append({
                "usuario": usuario,
                "juego": partida["juego"],
                "puntaje": partida["puntaje"]
            })

    # Ordenamiento por selección, de mayor a menor puntaje
    for i in range(len(todas_las_partidas)):

        indice_mayor = i

        for j in range(i + 1, len(todas_las_partidas)):

            if todas_las_partidas[j]["puntaje"] > todas_las_partidas[indice_mayor]["puntaje"]:
                indice_mayor = j

        todas_las_partidas[i], todas_las_partidas[indice_mayor] = (
            todas_las_partidas[indice_mayor], todas_las_partidas[i]
        )

    return todas_las_partidas[:10]


def ver_puntajes(usuario):
    """
    Muestra el top 10 de mejores puntajes registrados en todo el
    sistema, ordenados de mayor a menor.

    Parámetro: usuario (string) con el nombre del usuario logueado
    (se usa solo para resaltarlo en el listado).

    No devuelve nada.
    """

    top_10 = obtener_top_10()

    print("\n🏆══════════════════════════════🏆")
    print("        TOP 10 PUNTAJES")
    print("🏆══════════════════════════════🏆")

    if len(top_10) == 0:
        print("📭 Todavía no hay partidas jugadas.")
        return

    posicion = 1

    for partida in top_10:

        marca = " 👈 (vos)" if partida["usuario"] == usuario else ""

        print(f"{posicion}️⃣ {partida['usuario']} - {partida['juego']} - "
              f"{partida['puntaje']} pts{marca}")

        posicion += 1


# ESTADÍSTICAS (ADMINISTRADOR)

def promedio_edad():
    """Calcula y muestra el promedio de edad de todos los usuarios."""

    suma_edades = 0
    cantidad = 0

    for datos in usuarios.values():
        suma_edades += datos["edad"]
        cantidad += 1

    promedio = suma_edades / cantidad
    print(f"📊 Promedio de edad: {promedio:.2f} años")


def usuario_mas_joven():
    """Determina y muestra el usuario de menor edad."""

    nombre_mas_joven = ""
    menor_edad = None

    for usuario, datos in usuarios.items():

        if menor_edad is None or datos["edad"] < menor_edad:
            menor_edad = datos["edad"]
            nombre_mas_joven = usuario

    print(f"🐣 Usuario más joven: {nombre_mas_joven} ({menor_edad} años)")


def usuario_mayor_edad():
    """Determina y muestra el usuario de mayor edad."""

    nombre_mayor = ""
    mayor_edad = None

    for usuario, datos in usuarios.items():

        if mayor_edad is None or datos["edad"] > mayor_edad:
            mayor_edad = datos["edad"]
            nombre_mayor = usuario

    print(f"👴 Usuario de mayor edad: {nombre_mayor} ({mayor_edad} años)")


def cantidad_total_usuarios():
    """Muestra la cantidad total de usuarios registrados."""

    print(f"👥 Cantidad total de usuarios: {len(usuarios)}")


def usuarios_mayores_de(edad_limite):
    """Muestra la cantidad de usuarios mayores a una edad determinada."""

    cantidad = 0

    for datos in usuarios.values():

        if datos["edad"] > edad_limite:
            cantidad += 1

    print(f"🔢 Usuarios mayores de {edad_limite} años: {cantidad}")


def buscar_usuario_por_nombre(nombre_buscado):
    """Busca si existe un usuario con un nombre específico."""

    if nombre_buscado in usuarios:
        print(f"✅ El usuario '{nombre_buscado}' existe en el sistema.")
    else:
        print(f"❌ El usuario '{nombre_buscado}' no está registrado.")


def listado_completo_usuarios():
    """Muestra el listado completo de usuarios (reutiliza ver_usuarios)."""

    ver_usuarios()


def usuario_con_mas_partidas():
    """Determina qué usuario jugó la mayor cantidad de partidas."""

    nombre_mas_activo = ""
    mayor_cantidad = -1

    for usuario, datos in usuarios.items():

        cantidad_partidas = len(datos["puntajes"])

        if cantidad_partidas > mayor_cantidad:
            mayor_cantidad = cantidad_partidas
            nombre_mas_activo = usuario

    print(f"🎮 Usuario con más partidas jugadas: {nombre_mas_activo} "
          f"({mayor_cantidad} partidas)")


def mejor_puntaje_historico():
    """Muestra el mejor puntaje histórico registrado en todo el sistema."""

    top_10 = obtener_top_10()

    if len(top_10) == 0:
        print("📭 Todavía no hay partidas jugadas.")
        return

    mejor = top_10[0]
    print(f"⭐ Mejor puntaje histórico: {mejor['usuario']} con "
          f"{mejor['puntaje']} pts en {mejor['juego']}")


def cantidad_jugadores_vs_admins():
    """Muestra cuántos usuarios son jugadores y cuántos son administradores."""

    cantidad_jugadores = 0
    cantidad_admins = 0

    for datos in usuarios.values():

        if datos["tipo"] == "jugador":
            cantidad_jugadores += 1
        elif datos["tipo"] == "admin":
            cantidad_admins += 1

    print(f"🎮 Jugadores: {cantidad_jugadores} | 👑 Administradores: {cantidad_admins}")


def ver_estadisticas():
    """
    Muestra un submenú con distintas estadísticas sobre los usuarios
    registrados en el sistema, y ejecuta la opción elegida.

    No recibe parámetros ni devuelve nada.
    """

    while True:

        print("""
    📊══════════════════════════════📊
            ESTADÍSTICAS
    📊══════════════════════════════📊

    1️⃣ Promedio de edad
    2️⃣ Usuario más joven
    3️⃣ Usuario de mayor edad
    4️⃣ Cantidad total de usuarios
    5️⃣ Usuarios mayores de una edad determinada
    6️⃣ Buscar usuario por nombre
    7️⃣ Listado completo de usuarios
    8️⃣ Usuario con más partidas jugadas
    9️⃣ Mejor puntaje histórico
    🔟 Cantidad de jugadores vs administradores
    0️⃣ Volver al menú anterior
        """)

        opcion = input("➡️ Seleccione una opción: ")

        if opcion == "1":
            promedio_edad()

        elif opcion == "2":
            usuario_mas_joven()

        elif opcion == "3":
            usuario_mayor_edad()

        elif opcion == "4":
            cantidad_total_usuarios()

        elif opcion == "5":

            edad_texto = input("🎂 Ingrese la edad límite: ")

            if edad_texto.isdigit():
                usuarios_mayores_de(int(edad_texto))
            else:
                print("⚠️ Ingrese un número válido.")

        elif opcion == "6":

            nombre = input("🔎 Ingrese el nombre a buscar: ")
            buscar_usuario_por_nombre(nombre)

        elif opcion == "7":
            listado_completo_usuarios()

        elif opcion == "8":
            usuario_con_mas_partidas()

        elif opcion == "9":
            mejor_puntaje_historico()

        elif opcion == "10":
            cantidad_jugadores_vs_admins()

        elif opcion == "0":
            break

        else:
            print("❌ Opción inválida.")
