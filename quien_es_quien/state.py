#import reflex as rx
import random


# Caracteristicas de personajes.

class caracteristicas_personajes:
    def __init__(self, nombre, color_cabello, color_ojos, genero, accesorios = False, barba = False, mejillas = False, expresion = False):
        self.nombre = nombre
        self.color_cabello = color_cabello
        self.color_ojos = color_ojos
        self.genero = genero
        self.accesorios = accesorios
        self.barba = barba
        self.mejillas = mejillas
        self.expresion = expresion  
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Cabello: {self.color_cabello}, Ojos: {self.color_ojos}, Género: {self.genero}, Accesorios: {self.accesorios}, Barba: {self.barba}, Mejillas: {self.mejillas}, Expresion: {self.expresion}"

personajes = [
    caracteristicas_personajes("Susan", color_cabello="blanco", color_ojos="marrones", genero="femenino", expresion="sonrisa"),
    caracteristicas_personajes("Claire", color_cabello="pelirrojo", color_ojos="marrones", genero="femenino", accesorios=["sombrero", "gafas"], expresion="sonrisa"),
    caracteristicas_personajes("David", color_cabello="rubio", color_ojos="castaños", genero="masculino", barba=True),
    caracteristicas_personajes("Anne", color_cabello="negro", color_ojos="marrones", genero="femenino", accesorios=["pendientes"], expresion="seria"),
    caracteristicas_personajes("Robert", color_cabello="castaño", color_ojos="azules", genero="masculino", mejillas="sonrojadas"),
    caracteristicas_personajes("Anita", color_cabello="rubio", color_ojos="azules", genero="femenino", accesorios=["lazos"], expresion="sonrisa"),
    caracteristicas_personajes("Joe", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=["gafas"], mejillas="redondeadas"),
    caracteristicas_personajes("George", color_cabello="blanco", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="seria"),
    caracteristicas_personajes("Bill", color_cabello="calvo", color_ojos="marrones", genero="masculino", barba=True, mejillas="gordas"),
    caracteristicas_personajes("Alfred", color_cabello="pelirrojo", color_ojos="azules", genero="masculino", expresion="triste"),
    caracteristicas_personajes("Max", color_cabello="negro", color_ojos="marro  nes", genero="masculino", accesorios=["bigote"]),
    caracteristicas_personajes("Tom", color_cabello="calvo", color_ojos="azules", genero="masculino", accesorios=["gafas"], expresion="seria"),
    caracteristicas_personajes("Alex", color_cabello="negro", color_ojos="marrones", genero="masculino", accesorios=["bigote"], expresion="sonrisa"),
    caracteristicas_personajes("Sam", color_cabello="calvo", color_ojos="marrones", genero="masculino", accesorios=["gafas"], mejillas="redondeadas"),
    caracteristicas_personajes("Richard", color_cabello="calvo", color_ojos="marrones", genero="masculino", barba=True),
    caracteristicas_personajes("Paul", color_cabello="blanco", color_ojos="marrones", genero="masculino", accesorios=["gafas"], expresion="seria"),
    caracteristicas_personajes("Maria", color_cabello="castaño", color_ojos="marrones", genero="femenino", accesorios=["pendientes"], expresion="sonrisa"),
    caracteristicas_personajes("Frans", color_cabello="pelirrojo", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    caracteristicas_personajes("Herman", color_cabello="calvo", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    caracteristicas_personajes("Bernard", color_cabello="castaño", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="serio"),
    caracteristicas_personajes("Philip", color_cabello="castaño", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    caracteristicas_personajes("Eric", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="sonrisa"),
    caracteristicas_personajes("Charles", color_cabello="rubio", color_ojos="marrones", genero="masculino", expresion="sonrisa"),
    caracteristicas_personajes("Peter", color_cabello="blanco", color_ojos="azul", genero="masculino", expresion="sonrisa")
]

# Personaje aleatorio

def escoger_carta():    

    return random.choice(personajes)


print(escoger_carta())