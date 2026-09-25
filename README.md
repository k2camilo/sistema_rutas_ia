# Instrucciones de uso

### 1. Ejecución del programa

Una vez descargado el proyecto, abrir la carpeta en Visual Studio Code o en una terminal.

Ejecutar el archivo principal:

```bash
python main.py
```

También puede utilizarse:

```bash
py main.py
```

### 2. Menú principal

Al iniciar el programa se mostrará el siguiente menú:

```text
1. Consultar una línea
2. Buscar una estación por nombre
3. Consultar una ruta
4. Salir
```

### 3. Consultar una línea

Seleccione la opción **1**.

Posteriormente, seleccione la línea que desea consultar:

* Línea Norte
* Línea Central
* Línea Sur

El sistema mostrará las estaciones correspondientes, indicando las estaciones con trasbordo y las conexiones rápidas disponibles.

### 4. Buscar una estación

Seleccione la opción **2**.

Ingrese el nombre completo o una parte del nombre de la estación.

El sistema mostrará las estaciones que coincidan con la búsqueda.

### 5. Consultar una ruta

Seleccione la opción **3**.

El sistema solicitará:

1. Estación de origen.
2. Estación de destino.

Una vez seleccionadas, el sistema buscará las rutas disponibles y mostrará la alternativa con menor tiempo estimado.

El resultado incluye:

* Tiempo estimado.
* Conexiones normales.
* Conexiones rápidas.
* Trasbordos.
* Recorrido de la ruta.
* Línea utilizada.

### 6. Salir

Para finalizar el programa, seleccione la opción **4** en el menú principal.

### Ejemplo

Para consultar una ruta:

```text
Origen: Portal Norte
Destino: Portal Americas
```

El sistema realizará la búsqueda y mostrará el resultado correspondiente.

> **Nota:** Los tiempos utilizados para seleccionar la ruta corresponden a los valores definidos para el modelo académico del proyecto.
