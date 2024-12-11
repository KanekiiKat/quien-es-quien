
class Personajes:
    def __init__(self, nombre, caracteristicas):
        self.nombre = nombre
        self.caracteristicas = caracteristicas
        
    def __str__(self):
        return f"{self.nombre} {self.caracteristicas}"

integrantes = [
    Personajes("alex", caracteristicas=["negro", "marrones", "masculino", "hombre", "bigote", "sonrisa", "felicidad", "bocagrande", "labiosgruesos", "orejasgrandes", "pelocorto", "narizpequena"]),
    Personajes("alfred", caracteristicas=["pelirrojo", "rojo", "azules", "celestes", "masculino", "hombre", "triste", "melancolico", "barba", "bocapequena", "orejasgrandes", "pelolargo", "rayaalmedio", "narizpequena"]),
    Personajes("anita", caracteristicas=["rubio", "pelorubio", "amarillo", "marrones", "cafe", "femenino", "mujer", "lazos", "monos", "sonrisa", "felicidad", "pelolargo", "mofletes", "mejillassonrosadas", "rayaalmedio", "narizpequena"]),
    Personajes("anne", caracteristicas=["negro", "oscuro", "pendientes", "marrones", "cafe", "femenino", "mujer", "aretes", "seria", "formal", "pelocorto", "narizgrande"]),
    Personajes("bernard", caracteristicas=["castano", "pelocastano", "marron", "marrones", "cafe", "masculino", "hombre", "sombrero", "gorra", "serio", "formal", "bocapequena", "cejasfinas", "narizgrande"]),
    Personajes("bill", caracteristicas=["calvo", "marrones", "cafe", "masculino", "hombre", "barba", "gordas", "anchas", "pelirrojo", "rojo", "orejasgrandes", "mofletes", "mejillassonrosadas", "bocapequena", "narizpequena"]),
    Personajes("charles", caracteristicas=["rubio", "pelorubio", "amarillo", "marrones", "cafe", "masculino", "hombre", "sonrisa", "felicidad", "bigote", "bocagrande", "labiosgruesos", "orejasgrandes", "rayaallado", "narizpequena"]),
    Personajes("claire", caracteristicas=["pelirrojo", "pendientes", "rojo", "marrones", "cafe", "femenino", "mujer", "sombrero", "gorra", "gafas", "lentes", "sonrisa", "felicidad", "bocapequena", "narizpequena"]),
    Personajes("david", caracteristicas=["rubio", "pelorubio", "amarillo", "castanos", "marrones", "masculino", "hombre", "barba", "orejasgrandes", "rayaallado", "narizpequena"]),
    Personajes("eric", caracteristicas=["rubio", "pelorubio", "amarillo", "marrones", "cafe", "masculino", "hombre", "sombrero", "gorra", "sonrisa", "felicidad", "bocagrande", "narizpequena"]),
    Personajes("frans", caracteristicas=["pelirrojo", "rojo", "marrones", "cafe", "masculino", "hombre", "sonrisa", "felicidad", "pelocorto", "cejasgruesas", "bocapequena", "narizpequena"]),
    Personajes("george", caracteristicas=["blanco", "gris", "marrones", "cafe", "masculino", "hombre", "sombrero", "gorra", "seria", "formal", "caratriste", "peloblanco", "canas", "bocagrande", "narizpequena"]),
    Personajes("herman", caracteristicas=["calvo", "marrones", "cafe", "masculino", "hombre", "sonrisa", "felicidad", "pelirrojo", "rojo", "narizgrande", "ojosmarrones", "cejasgruesas"]),
    Personajes("joe", caracteristicas=["rubio", "pelorubio", "amarillo", "marrones", "cafe", "masculino", "hombre", "gafas", "lentes", "redondeadas", "circulares", "pelocorto", "bocapequena", "narizpequena"]),
    Personajes("maria", caracteristicas=["castano","pelocastano", "pendientes", "marron", "marrones", "cafe", "femenino", "mujer", "aretes", "sonrisa", "felicidad", "pelolargo", "sombrero", "bocapequena", "cejasfinas", "narizpequena"]),
    Personajes("max", caracteristicas=["negro", "oscuro", "marrones", "cafe", "masculino", "hombre", "bigote", "bocagrande", "labiosgruesos", "narizgrande", "orejasgrandes", "pelocorto"]),
    Personajes("paul", caracteristicas=["blanco", "gris", "marrones", "cafe", "masculino", "hombre", "gafas", "lentes", "seria", "formal", "peloblanco", "canas", "bocapequena", "orejasgrandes", "cejasgruesas", "rayaallado", "narizpequena"]),
    Personajes("peter", caracteristicas=["blanco", "gris", "azul", "celeste", "masculino", "hombre", "sonrisa", "felicidad", "canas", "peloblanco", "narizgrande", "cejasgruesas", "bocagrande", "labiosgruesos", "rayaallado"]),
    Personajes("philip", caracteristicas=["castano", "pelocastano", "marron", "marrones", "cafe", "masculino", "hombre", "sonrisa", "felicidad", "barba", "orejasgrandes", "mofletes", "mejillassonrosadas", "cejasfinas", "pelocorto", "narizpequena"]),
    Personajes("richard", caracteristicas=["calvo", "marrones", "cafe", "masculino", "hombre", "barba", "orejasgrandes", "bigote", "caraalargada", "narizpequena"]),
    Personajes("robert", caracteristicas=["castano", "pelocastano", "marron", "azules", "celestes", "masculino", "hombre", "sonrojadas", "ruborizadas", "caratriste", "orejasgrandes", "narizgrande", "rayaallado", "caraalargada", "mofletes", "mejillassonrosadas"]),
    Personajes("sam", caracteristicas=["calvo", "marrones", "cafe", "masculino", "hombre", "gafas", "lentes", "redondeadas", "circulares", "peloblanco", "canas", "bocapequena", "narizpequena"]),
    Personajes("susan", caracteristicas=["blanco", "gris", "marrones", "cafe", "femenino", "mujer", "sonrisa", "felicidad", "pelolargo", "canas", "labiosgruesos", "moflete s", "mejillassonrosadas", "narizpequena", "rayaallado"]),
    Personajes("tom", caracteristicas=["calvo", "azules", "celestes", "masculino", "hombre", "gafas", "lentes", "seria", "formal", "pelonegro", "caraalargada", "bocapequena", "narizpequena"]),
]
