
estaciones = [
    "Portal Norte",
    "Toberin",
    "Cardio Infantil",
    "Mazuren",
    "Calle 146",
    "Calle 142",
    "Alcala",
    "Prado",
    "Calle 127",
    "Pepe Sierra",
    "Calle 106",
    "Calle 100",
    "Virrey",
    "Calle 85",
    "Heroes",
    "Calle 76",
    "Calle 72",
    "Flores",
    "Calle 63",
    "Calle 57",
    "Marly",
    "Calle 45",
    "Calle 39",
    "Profamilia",
    "Calle 26",
    "Calle 22",
    "Calle 19",
    "Jimenez",
    "De la Sabana",
    "San Facon",
    "Ricaurte",
    "Carrera 32",
    "Zona Industrial",
    "Carrera 43",
    "Puente Aranda",
    "Carrera 53",
    "Pradera",
    "Marsella",
    "Mundo Aventura",
    "Mandalay",
    "Banderas",
    "Transversal 86",
    "Biblioteca Tintal",
    "Patio Bonito",
    "Portal Americas"
]


conexiones = {

    "Portal Norte": ["Toberin"],

    "Toberin": [
        "Portal Norte",
        "Cardio Infantil"
    ],

    "Cardio Infantil": [
        "Toberin",
        "Mazuren"
    ],

    "Mazuren": [
        "Cardio Infantil",
        "Calle 146"
    ],

    "Calle 146": [
        "Mazuren",
        "Calle 142"
    ],

    "Calle 142": [
        "Calle 146",
        "Alcala"
    ],

    "Alcala": [
        "Calle 142",
        "Prado"
    ],

    "Prado": [
        "Alcala",
        "Calle 127"
    ],

    "Calle 127": [
        "Prado",
        "Pepe Sierra"
    ],

    "Pepe Sierra": [
        "Calle 127",
        "Calle 106"
    ],

    "Calle 106": [
        "Pepe Sierra",
        "Calle 100"
    ],

    "Calle 100": [
        "Calle 106",
        "Virrey"
    ],

    "Virrey": [
        "Calle 100",
        "Calle 85"
    ],

    "Calle 85": [
        "Virrey",
        "Heroes"
    ],

    "Heroes": [
        "Calle 85",
        "Calle 76"
    ],

    "Calle 76": [
        "Heroes",
        "Calle 72"
    ],

    "Calle 72": [
        "Calle 76",
        "Flores"
    ],

    "Flores": [
        "Calle 72",
        "Calle 63"
    ],

    "Calle 63": [
        "Flores",
        "Calle 57"
    ],

    "Calle 57": [
        "Calle 63",
        "Marly"
    ],

    "Marly": [
        "Calle 57",
        "Calle 45"
    ],

    "Calle 45": [
        "Marly",
        "Calle 39"
    ],

    "Calle 39": [
        "Calle 45",
        "Profamilia"
    ],

    "Profamilia": [
        "Calle 39",
        "Calle 26"
    ],

    "Calle 26": [
        "Profamilia",
        "Calle 22"
    ],

    "Calle 22": [
        "Calle 26",
        "Calle 19"
    ],

    "Calle 19": [
        "Calle 22",
        "Jimenez"
    ],

    "Jimenez": [
        "Calle 19",
        "De la Sabana"
    ],

    "De la Sabana": [
        "Jimenez",
        "San Facon"
    ],

    "San Facon": [
        "De la Sabana",
        "Ricaurte"
    ],

    "Ricaurte": [
        "San Facon",
        "Carrera 32"
    ],

    "Carrera 32": [
        "Ricaurte",
        "Zona Industrial"
    ],

    "Zona Industrial": [
        "Carrera 32",
        "Carrera 43"
    ],

    "Carrera 43": [
        "Zona Industrial",
        "Puente Aranda"
    ],

    "Puente Aranda": [
        "Carrera 43",
        "Carrera 53"
    ],

    "Carrera 53": [
        "Puente Aranda",
        "Pradera"
    ],

    "Pradera": [
        "Carrera 53",
        "Marsella"
    ],

    "Marsella": [
        "Pradera",
        "Mundo Aventura"
    ],

    "Mundo Aventura": [
        "Marsella",
        "Mandalay"
    ],

    "Mandalay": [
        "Mundo Aventura",
        "Banderas"
    ],

    "Banderas": [
        "Mandalay",
        "Transversal 86"
    ],

    "Transversal 86": [
        "Banderas",
        "Biblioteca Tintal"
    ],

    "Biblioteca Tintal": [
        "Transversal 86",
        "Patio Bonito"
    ],

    "Patio Bonito": [
        "Biblioteca Tintal",
        "Portal Americas"
    ],

    "Portal Americas": [
        "Patio Bonito"
    ]
}


lineas = {

    "Linea Norte": [
        "Portal Norte",
        "Toberin",
        "Cardio Infantil",
        "Mazuren",
        "Calle 146",
        "Calle 142",
        "Alcala",
        "Prado",
        "Calle 127",
        "Pepe Sierra",
        "Calle 106",
        "Calle 100",
        "Virrey",
        "Calle 85",
        "Heroes",
        "Calle 76",
        "Calle 72"
    ],


    "Linea Central": [
        "Calle 72",
        "Flores",
        "Calle 63",
        "Calle 57",
        "Marly",
        "Calle 45",
        "Calle 39",
        "Profamilia",
        "Calle 26",
        "Calle 22",
        "Calle 19",
        "Jimenez",
        "De la Sabana",
        "San Facon",
        "Ricaurte"
    ],


    "Linea Sur": [
        "Ricaurte",
        "Carrera 32",
        "Zona Industrial",
        "Carrera 43",
        "Puente Aranda",
        "Carrera 53",
        "Pradera",
        "Marsella",
        "Mundo Aventura",
        "Mandalay",
        "Banderas",
        "Transversal 86",
        "Biblioteca Tintal",
        "Patio Bonito",
        "Portal Americas"
    ]
}

conexion_lineas = {

    "Linea Norte": {

        "Portal Norte": ["Toberin"],

        "Toberin": [
            "Portal Norte",
            "Cardio Infantil"
        ],

        "Cardio Infantil": [
            "Toberin",
            "Mazuren"
        ],

        "Mazuren": [
            "Cardio Infantil",
            "Calle 146"
        ],

        "Calle 146": [
            "Mazuren",
            "Calle 142"
        ],

        "Calle 142": [
            "Calle 146",
            "Alcala"
        ],

        "Alcala": [
            "Calle 142",
            "Prado"
        ],

        "Prado": [
            "Alcala",
            "Calle 127"
        ],

        "Calle 127": [
            "Prado",
            "Pepe Sierra"
        ],

        "Pepe Sierra": [
            "Calle 127",
            "Calle 106"
        ],

        "Calle 106": [
            "Pepe Sierra",
            "Calle 100"
        ],

        "Calle 100": [
            "Calle 106",
            "Virrey"
        ],

        "Virrey": [
            "Calle 100",
            "Calle 85"
        ],

        "Calle 85": [
            "Virrey",
            "Heroes"
        ],

        "Heroes": [
            "Calle 85",
            "Calle 76"
        ],

        "Calle 76": [
            "Heroes",
            "Calle 72"
        ],

        "Calle 72": [
            "Calle 76"
        ]
    },
    
    "Linea Central": {

        "Calle 72": ["Flores"],

        "Flores": [
            "Calle 72",
            "Calle 63"
        ],

        "Calle 63": [
            "Flores",
            "Calle 57"
        ],

        "Calle 57": [
            "Calle 63",
            "Marly"
        ],

        "Marly": [
            "Calle 57",
            "Calle 45"
        ],

        "Calle 45": [
            "Marly",
            "Calle 39"
        ],

        "Calle 39": [
            "Calle 45",
            "Profamilia"
        ],

        "Profamilia": [
            "Calle 39",
            "Calle 26"
        ],

        "Calle 26": [
            "Profamilia",
            "Calle 22"
        ],

        "Calle 22": [
            "Calle 26",
            "Calle 19"
        ],

        "Calle 19": [
            "Calle 22",
            "Jimenez"
        ],

        "Jimenez": [
            "Calle 19",
            "De la Sabana"
        ],

        "De la Sabana": [
            "Jimenez",
            "San Facon"
        ],

        "San Facon": [
            "De la Sabana",
            "Ricaurte"
        ],

        "Ricaurte": [
            "San Facon"
        ]
    },
    
    "Linea Sur": {

        "Ricaurte": ["Carrera 32"],

        "Carrera 32": [
            "Ricaurte",
            "Zona Industrial"
        ],

        "Zona Industrial": [
            "Carrera 32",
            "Carrera 43"
        ],

        "Carrera 43": [
            "Zona Industrial",
            "Puente Aranda"
        ],

        "Puente Aranda": [
            "Carrera 43",
            "Carrera 53"
        ],

        "Carrera 53": [
            "Puente Aranda",
            "Pradera"
        ],

        "Pradera": [
            "Carrera 53",
            "Marsella"
        ],

        "Marsella": [
            "Pradera",
            "Mundo Aventura"
        ],

        "Mundo Aventura": [
            "Marsella",
            "Mandalay"
        ],

        "Mandalay": [
            "Mundo Aventura",
            "Banderas"
        ],

        "Banderas": [
            "Mandalay",
            "Transversal 86"
        ],

        "Transversal 86": [
            "Banderas",
            "Biblioteca Tintal"
        ],

        "Biblioteca Tintal": [
            "Transversal 86",
            "Patio Bonito"
        ],

        "Patio Bonito": [
            "Biblioteca Tintal",
            "Portal Americas"
        ],

        "Portal Americas": [
            "Patio Bonito"
        ]
    }
}

conexiones_rapidas = {
    "Linea Norte": {
        "Calle 100": ["Calle 85"],
        "Calle 85": ["Calle 72"]
    },
    
    "Linea Central": {
        "Calle 39": ["Calle 22"],
        "Calle 22": ["Ricaurte"]
    },
    
    "Linea Sur": {
        "Ricaurte": ["Zona Industrial"],
        "Carrera 32": ["Puente Aranda"],
    }
}

trasbordos = {

    "Calle 72": [
        "Linea Norte",
        "Linea Central"
    ],

    "Ricaurte": [
        "Linea Central",
        "Linea Sur"
    ]
}

tiempo_estacion = 5
tiempo_transbordo = 8
tiempo_conexion_rapida = 3
