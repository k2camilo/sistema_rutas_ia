from conocimiento import conexiones_rapidas, conexion_lineas, estaciones, lineas, trasbordos

def obtener_linea(estacion):
    
    linea = []
    
    for nombre_linea, estaciones_linea in lineas.items():
        if estacion in estaciones_linea:
            linea.append(nombre_linea)
    return linea

def tiene_trasbordos(estacion):
    
    for nombre_trasbordo, lineas_trasbordo in trasbordos.items():
        if estacion == nombre_trasbordo:
            return lineas_trasbordo

    return []


def obtener_lineas_trasbordos(estacion, linea_actual):

    lineas_disponibles = tiene_trasbordos(estacion)

    lineas_trasbordo = []

    for linea in lineas_disponibles:
        if linea != linea_actual:
            lineas_trasbordo.append(linea)

    return lineas_trasbordo


def obtener_siguientes_estaciones(estacion, linea):

    siguientes = conexion_lineas[linea][estacion].copy()
    
    if estacion in conexiones_rapidas.get(linea, {}):
        siguientes += conexiones_rapidas[linea][estacion]

    return siguientes

def estacion_valida(estacion):

    return estacion in estaciones