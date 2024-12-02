import reflex as rx
import random
from quien_es_quien import personajes

# Personaje aleatorio

def escoger_carta():    

    return random.choice(personajes.integrantes).nombre

# Enviar el mensaje del input


class State(rx.State):

    pregunta_usuario: str = ""

    @rx.event
    def escribir_pregunta_usuario(self, value):
        self.pregunta_usuario = value

    def mensaje_usuario(self):
        if self.pregunta_usuario:
            print(self.pregunta_usuario)
            self.pregunta_usuario = ""

