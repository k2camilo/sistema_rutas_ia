from collections import deque
from conocimiento import conexiones_rapidas, tiempo_transbordo, tiempo_estacion, tiempo_conexion_rapida, estaciones
from reglas import obtener_linea, obtener_lineas_trasbordos, obtener_siguientes_estaciones


def buscar_rutas(origen, destino):
    
    rutas = []
    
    cola = deque()
    
    linea_origen = obtener_linea(origen)[0]
    
    estado_inicial = (origen, linea_origen)
    
    cola.append([(estado_inicial)])
    
    while cola:
        
        camino = cola.popleft()
        
        estado_actual = camino[-1]
        
        estacion_actual = estado_actual[0]
        linea_actual = estado_actual[1]

        if estacion_actual == destino:

            rutas.append(camino)

            continue
        
        siguientes = obtener_siguientes_estaciones(estacion_actual, linea_actual)
        
        for siguiente in siguientes:
            nuevo_estado = (siguiente, linea_actual)
            
            if nuevo_estado not in camino:
                nuevo_camino = camino + [nuevo_estado]
                cola.append(nuevo_camino)
        
        lineas_transbordo = obtener_lineas_trasbordos(estacion_actual, linea_actual)
        
        for nueva_linea in lineas_transbordo:
            nuevo_estado = (estacion_actual, nueva_linea)
            
            if nuevo_estado not in camino:
                nuevo_camino = camino + [nuevo_estado]
                cola.append(nuevo_camino)
    
    return rutas

def evaluar_rutas(rutas):

    rutas_evaluadas = []

    for ruta in rutas:

        tiempo = calcular_tiempo(ruta)

        rutas_evaluadas.append((ruta, tiempo))

    return rutas_evaluadas
    
def seleccionar_mejor_ruta(rutas_evaluadas):

    mejor_ruta = None
    menor_tiempo = None

    for ruta, tiempo in rutas_evaluadas:

        if menor_tiempo is None or tiempo < menor_tiempo:

            mejor_ruta = ruta
            menor_tiempo = tiempo

    return mejor_ruta, menor_tiempo


def calcular_tiempo(ruta):

    tiempo = 0

    for i in range(1, len(ruta)):

        estado_anterior = ruta[i - 1]
        estado_actual = ruta[i]

        estacion_anterior = estado_anterior[0]
        linea_anterior = estado_anterior[1]

        estacion_actual = estado_actual[0]
        linea_actual = estado_actual[1]

        if estacion_anterior == estacion_actual and linea_anterior != linea_actual:

            tiempo += tiempo_transbordo

        elif estacion_actual in conexiones_rapidas.get(linea_actual, {}).get(estacion_anterior, []):

            tiempo += tiempo_conexion_rapida

        else:

            tiempo += tiempo_estacion

    return tiempo


def convertir_tiempo(ruta):
    
    minutos = calcular_tiempo(ruta)
    horas = minutos // 60
    minutos = minutos % 60
    if horas > 0: 
        return f"{horas} hora(s) y {minutos} minutos"
    
    return f"{minutos} minutos"

def resumir_ruta(ruta):

    cantidad_conexiones_normales = 0
    cantidad_conexiones_rapidas = 0
    cantidad_trasbordos = 0

    for i in range(1, len(ruta)):

        estado_anterior = ruta[i - 1]
        estado_actual = ruta[i]

        estacion_anterior = estado_anterior[0]
        linea_anterior = estado_anterior[1]

        estacion_actual = estado_actual[0]
        linea_actual = estado_actual[1]

        # Verificar si es un trasbordo
        if estacion_anterior == estacion_actual and linea_anterior != linea_actual:

            cantidad_trasbordos += 1

        # Verificar si es una conexión rápida
        elif estacion_actual in conexiones_rapidas.get(linea_actual, {}).get(estacion_anterior, []):

            cantidad_conexiones_rapidas += 1

        # Si no es trasbordo ni conexión rápida, es normal
        else:

            cantidad_conexiones_normales += 1

    return {
        "conexiones_normales": cantidad_conexiones_normales,
        "conexiones_rapidas": cantidad_conexiones_rapidas,
        "trasbordos": cantidad_trasbordos,
        "tiempo_total": calcular_tiempo(ruta)
    }
    
def buscar_estaciones(texto):

    resultados = []

    texto = texto.lower()

    for estacion in estaciones:

        if texto in estacion.lower():
            resultados.append(estacion)

    return resultados