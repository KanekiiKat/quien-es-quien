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
    def __init__(self, nombre, color_pelo, color_ojos, genero, accesorios, barba, mejillas, boca):
        self.nombre = nombre
        self.color_cabello = color_pelo
        self.color_ojos = color_ojos
        self.genero = genero
        self.accesorios = accesorios
        self.barba = barba
        self.mejillas = mejillas
        self.boca = boca

    def __str__(self):
        return f"Nombre: {self.nombre}, Cabello: {self.color_cabello}, Ojos: {self.color_ojos}, Género: {self.genero}, Accesorios: {self.accesorios}, Barba: {self.barba}, Mejillas: {self.mejillas}, Boca: {self.boca}"