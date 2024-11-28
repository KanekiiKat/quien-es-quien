#import reflex as rx
import random

# Personajes 

personajes = ['Susan', 'Claire', 'David', 'Anne', 'Robert', 'Anita',
              'Joe', 'George', 'Bill', 'Alfred', 'Max', 'Tom',
              'Alex', 'Sam', 'Richard', 'Paul', 'Maria', ' Frans' ,
              'Herman' , 'Bernardo', 'Philip', 'Eric', 'Charlis', 'Peter']

# Personaje aleatorio

def escoger_carta():
    return personajes[random.randint(0, 23)]

# Caracteristicas de personajes.

class caracteristicas_personajes:
    def __init__(self, nombre, color_pelo, color_ojos, genero, accesorios, barba, mejillas, expresion):
        self.nombre = nombre
        self.color_cabello = color_pelo
        self.color_ojos = color_ojos
        self.genero = genero
        self.accesorios = accesorios if accesorios else []
        self.barba = barba if barba else []
        self.mejillas = mejillas
        self.expresion = expresion

    def __str__(self):
        return f"Nombre: {self.nombre}, Cabello: {self.color_cabello}, Ojos: {self.color_ojos}, Género: {self.genero}, Accesorios: {self.accesorios}, Barba: {self.barba}, Mejillas: {self.mejillas}, expresion: {self.expresion}"

personajes = [
    personajes("Susan", color_cabello="blanco", color_ojos="marrones", genero="femenino", expresion="sonrisa"),
    personajes("Claire", color_cabello="pelirrojo", color_ojos="marrones", genero="femenino", accesorios=["sombrero", "gafas"], expresion="sonrisa"),
    personajes("David", color_cabello="rubio", color_ojos="castaños", genero="masculino", barba=True),
    personajes("Anne", color_cabello="negro", color_ojos="marrones", genero="femenino", accesorios=["pendientes"], expresion="seria"),
    personajes("Robert", color_cabello="castaño", color_ojos="azules", genero="masculino", mejillas="sonrojadas"),
    personajes("Anita", color_cabello="rubio", color_ojos="azules", genero="femenino", accesorios=["lazos"], expresion="sonrisa"),
    personajes("Joe", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=["gafas"], mejillas="redondeadas"),
    personajes("George", color_cabello="blanco", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="seria"),
    personajes("Bill", color_cabello="calvo", color_ojos="marrones", genero="masculino", barba=True, mejillas="gordas"),
    personajes("Alfred", color_cabello="pelirrojo", color_ojos="azules", genero="masculino", expresion="triste"),
    personajes("Max", color_cabello="negro", color_ojos="marrones", genero="masculino", accesorios=["bigote"]),
    personajes("Tom", color_cabello="calvo", color_ojos="azules", genero="masculino", accesorios=["gafas"], expresion="seria"),
    personajes("Alex", color_cabello="negro", color_ojos="marrones", genero="masculino", accesorios=["bigote"], expresion="sonrisa"),
    personajes("Sam", color_cabello="calvo", color_ojos="marrones", genero="masculino", accesorios=["gafas"], mejillas="redondeadas"),
    personajes("Richard", color_cabello="calvo", color_ojos="marrones", genero="masculino", barba=True),
    personajes("Paul", color_cabello="blanco", color_ojos="marrones", genero="masculino", accesorios=["gafas"], expresion="seria"),
    personajes("Maria", color_cabello="castaño", color_ojos="marrones", genero="femenino", accesorios=["pendientes"], expresion="sonrisa"),
    personajes("Frans", color_cabello="pelirrojo", color_ojos="marrones", genero="masculino", accesorios=[], expresion="sonrisa"),
    personajes("Herman", color_cabello="calvo", color_ojos="marrones", genero="masculino", accesorios=[], expresion="sonrisa"),
    personajes("Bernard", color_cabello="castaño", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="serio"),
    personajes("Philip", color_cabello="castaño", color_ojos="marrones", genero="masculino", accesorios=[], expresion="sonrisa"),
    personajes("Eric", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=["sombrero"], expresion="sonrisa"),
    personajes("Charles", color_cabello="rubio", color_ojos="marrones", genero="masculino", accesorios=[], expresion="sonrisa"),
    personajes("Peter", color_cabello="blanco", color_ojos="azul", genero="masculino", accesorios=[], expresion="sonrisa")
]