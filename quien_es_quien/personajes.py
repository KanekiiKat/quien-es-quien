
class Personajes:
    def __init__(self, nombre, caracteristicas):
        self.nombre = nombre
        self.caracteristicas = caracteristicas
        
    def __str__(self):
        return f"{self.nombre} {self.caracteristicas}"

integrantes = [
    Personajes("alex", caracteristicas=["negro", "marrones", "masculino", "hombre", "bigote", "sonrisa", "felicidad"]),
    Personajes("alfred", caracteristicas=["pelirrojo", "rojo", "azules", "celestes", "masculino", "hombre", "triste", "melancólico"]),
    Personajes("anita", caracteristicas=["rubio", "amarillo", "azules", "celestes", "femenino", "mujer", "lazos", "moños", "sonrisa", "felicidad"]),
    Personajes("anne", caracteristicas=["negro", "oscuro", "marrones", "café", "femenino", "mujer", "pendientes", "aretes", "seria", "formal"]),
    Personajes("bernard", caracteristicas=["castano", "marron", "marrones", "café", "masculino", "hombre", "sombrero", "gorra", "serio", "formal"]),
    Personajes("bill", caracteristicas=["calvo", "marrones", "café", "masculino", "hombre", "barba", "gordas", "anchas"]),
    Personajes("charles", caracteristicas=["rubio", "amarillo", "marrones", "café", "masculino", "hombre", "sonrisa", "felicidad"]),
    Personajes("claire", caracteristicas=["pelirrojo", "rojo", "marrones", "café", "femenino", "mujer", "sombrero", "gorra", "gafas", "lentes", "sonrisa", "felicidad"]),
    Personajes("david", caracteristicas=["rubio", "amarillo", "castanos", "marrones", "masculino", "hombre", "barba", ]),
    Personajes("eric", caracteristicas=["rubio", "amarillo", "marrones", "café", "masculino", "hombre", "sombrero", "gorra", "sonrisa", "felicidad"]),
    Personajes("frans", caracteristicas=["pelirrojo", "rojo", "marrones", "café", "masculino", "hombre", "sonrisa", "felicidad"]),
    Personajes("george", caracteristicas=["blanco", "gris", "marrones", "café", "masculino", "hombre", "sombrero", "gorra", "seria", "formal"]),
    Personajes("herman", caracteristicas=["calvo", "marrones", "café", "masculino", "hombre", "sonrisa", "felicidad"]),
    Personajes("joe", caracteristicas=["rubio", "amarillo", "marrones", "café", "masculino", "hombre", "gafas", "lentes", "redondeadas", "circulares"]),
    Personajes("maria", caracteristicas=["castano", "marron", "marrones", "café", "femenino", "mujer", "pendientes", "aretes", "sonrisa", "felicidad"]),
    Personajes("max", caracteristicas=["negro", "oscuro", "marrones", "café", "masculino", "hombre", "bigote", ]),
    Personajes("paul", caracteristicas=["blanco", "gris", "marrones", "café", "masculino", "hombre", "gafas", "lentes", "seria", "formal"]),
    Personajes("peter", caracteristicas=["blanco", "gris", "azul", "celeste", "masculino", "hombre", "sonrisa", "felicidad"]),
    Personajes("philip", caracteristicas=["castano", "marron", "marrones", "café", "masculino", "hombre", "sonrisa", "felicidad"]),
    Personajes("richard", caracteristicas=["calvo", "marrones", "café", "masculino", "hombre", "barba", ]),
    Personajes("robert", caracteristicas=["castano", "marron", "azules", "celestes", "masculino", "hombre", "sonrojadas", "ruborizadas"]),
    Personajes("sam", caracteristicas=["calvo", "marrones", "café", "masculino", "hombre", "gafas", "lentes", "redondeadas", "circulares"]),
    Personajes("susan", caracteristicas=["blanco", "gris", "marrones", "café", "femenino", "mujer", "sonrisa", "felicidad"]),
    Personajes("tom", caracteristicas=["calvo", "azules", "celestes", "masculino", "hombre", "gafas", "lentes", "seria", "formal"]),
]
