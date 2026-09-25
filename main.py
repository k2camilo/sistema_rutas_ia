from conocimiento import lineas, conexiones_rapidas, trasbordos
from busqueda import buscar_estaciones, convertir_tiempo, buscar_rutas, evaluar_rutas, seleccionar_mejor_ruta, resumir_ruta


def mostrar_menu():
    print("\n" + "=" * 55)
    print("          SISTEMA INTELIGENTE DE RUTAS")
    print("=" * 55)

    print("\nEl sistema de transporte cuenta con 3 líneas:")
    print("1. Línea Norte")
    print("2. Línea Central")
    print("3. Línea Sur")

    print("\n¿Qué desea hacer?")
    print("1. Consultar una línea")
    print("2. Buscar una estación por nombre")
    print("3. Consultar una ruta")
    print("4. Salir")


def consultar_linea():

    print("\n" + "=" * 55)
    print("                 CONSULTAR LÍNEA")
    print("=" * 55)

    print("\nSeleccione la línea que desea consultar:")
    print("1. Línea Norte")
    print("2. Línea Central")
    print("3. Línea Sur")
    print("4. Volver")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "4":
        return

    if opcion == "1":
        nombre_linea = "Linea Norte"

    elif opcion == "2":
        nombre_linea = "Linea Central"

    elif opcion == "3":
        nombre_linea = "Linea Sur"

    else:
        print("\nOpción no válida.")
        return

    print("\n" + "-" * 55)
    print(f"              {nombre_linea.upper()}")
    print("-" * 55)

    estaciones_linea = lineas[nombre_linea]

    cantidad_trasbordos = 0
    cantidad_conexiones_rapidas = 0

    for numero, estacion in enumerate(estaciones_linea, start=1):

        etiquetas = []

        # Verificar si la estación permite trasbordo
        if estacion in trasbordos:

            etiquetas.append("TRASBORDO")
            cantidad_trasbordos += 1

        # Verificar si desde la estación existe una conexión rápida
        if estacion in conexiones_rapidas.get(nombre_linea, {}):

            destino_rapido = conexiones_rapidas[nombre_linea][estacion]

            etiquetas.append(
                f"CONEXIÓN RÁPIDA → {', '.join(destino_rapido)}"
            )

            cantidad_conexiones_rapidas += 1

        # Mostrar estación
        if etiquetas:

            print(
                f"{numero}. {estacion} "
                f"[{', '.join(etiquetas)}]"
            )

        else:

            print(f"{numero}. {estacion}")

    print("-" * 55)

    print(f"Total de estaciones: {len(estaciones_linea)}")
    print(f"Trasbordos disponibles: {cantidad_trasbordos}")
    print(f"Conexiones rápidas: {cantidad_conexiones_rapidas}")

    print("-" * 55)


def buscar_estacion():

    print("\n" + "=" * 55)
    print("              BUSCAR ESTACIÓN")
    print("=" * 55)

    texto = input(
        "\nIngrese el nombre o parte del nombre: "
    )

    resultados = buscar_estaciones(texto)

    if not resultados:

        print("\nNo se encontraron estaciones.")
        return

    print("\nEstaciones encontradas:")
    print("-" * 55)

    for numero, estacion in enumerate(resultados, start=1):

        print(f"{numero}. {estacion}")

    print("-" * 55)


def seleccionar_estacion(mensaje):

    while True:

        texto = input(mensaje)

        resultados = buscar_estaciones(texto)

        if not resultados:

            print("\nNo se encontraron estaciones.")
            print("Intente nuevamente.")

            continue

        # Si solamente existe una coincidencia,
        # se selecciona automáticamente
        if len(resultados) == 1:

            return resultados[0]

        # Si existen varias coincidencias,
        # se muestran para que el usuario seleccione
        print("\nSe encontraron varias estaciones:")
        print("-" * 55)

        for numero, estacion in enumerate(
            resultados,
            start=1
        ):

            print(f"{numero}. {estacion}")

        print("-" * 55)

        opcion = input(
            "Seleccione el número de la estación: "
        )

        if opcion.isdigit():

            numero = int(opcion)

            if 1 <= numero <= len(resultados):

                return resultados[numero - 1]

        print("\nSelección no válida.")
        print("Intente nuevamente.")


def consultar_ruta():

    print("\n" + "=" * 55)
    print("                CONSULTAR RUTA")
    print("=" * 55)

    # Seleccionar estación de origen
    origen = seleccionar_estacion(
        "\nIngrese la estación de origen: "
    )

    print(f"\nOrigen seleccionado: {origen}")

    # Seleccionar estación de destino
    destino = seleccionar_estacion(
        "Ingrese la estación de destino: "
    )

    print(f"Destino seleccionado: {destino}")

    # Validar que no sean iguales
    if origen == destino:

        print("\nEl origen y el destino son iguales.")
        print("No es necesario realizar un recorrido.")

        return

    print("\nBuscando rutas...")

    # Buscar todas las rutas posibles
    rutas = buscar_rutas(
        origen,
        destino
    )

    if not rutas:

        print("\nNo existe una ruta disponible entre")
        print("las estaciones seleccionadas.")

        return

    print(f"\nRutas encontradas: {len(rutas)}")

    # Evaluar las rutas encontradas
    rutas_evaluadas = evaluar_rutas(rutas)

    # Seleccionar la ruta con menor tiempo
    mejor_ruta, menor_tiempo = seleccionar_mejor_ruta(
        rutas_evaluadas
    )

    if mejor_ruta is None:

        print("\nNo fue posible determinar una ruta.")

        return

    # Obtener información adicional
    resumen = resumir_ruta(
        mejor_ruta
    )

    print("\n" + "=" * 55)
    print("                 MEJOR RUTA")
    print("=" * 55)

    print(f"\nOrigen: {origen}")
    print(f"Destino: {destino}")

    print(
        "\nTiempo estimado:",
        convertir_tiempo(mejor_ruta)
    )

    print("\nResumen:")

    print(
        "Conexiones normales:",
        resumen["conexiones_normales"]
    )

    print(
        "Conexiones rápidas:",
        resumen["conexiones_rapidas"]
    )

    print(
        "Trasbordos:",
        resumen["trasbordos"]
    )

    print("\nRecorrido:")
    print("-" * 55)

    for estacion, linea in mejor_ruta:

        print(
            f"- {estacion} | {linea}"
        )

    print("-" * 55)


# =========================================================
# PROGRAMA PRINCIPAL
# =========================================================

while True:

    mostrar_menu()

    opcion = input(
        "\nSeleccione una opción: "
    )

    if opcion == "1":

        consultar_linea()

    elif opcion == "2":

        buscar_estacion()

    elif opcion == "3":

        consultar_ruta()

    elif opcion == "4":

        print("\nGracias por utilizar el sistema.")
        print("Hasta pronto.")

        break

    else:

        print("\nOpción no válida.")
        print("Por favor, seleccione una opción del 1 al 4.")