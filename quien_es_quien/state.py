import reflex as rx
import random
from quien_es_quien import personajes
import reflex as rx
from quien_es_quien import quien_es_quien

# Personaje aleatorio

def escoger_carta():    

    return random.choice(personajes.integrantes).nombre

# Enviar el mensaje del input

class State(rx.State):

    texto: str

    @rx.event
    def pregunta(self):
        self.pregunta = self

    @rx.event
    def buscar_caracteristica(self):
        print(self.texto)
