import reflex as rx
import random
from quien_es_quien import personajes
import unicodedata

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
            pregunta_limpia = self.limpiar_palabra(self.pregunta_usuario)
            print(pregunta_limpia)
            self.pregunta_usuario = ""

    def limpiar_palabra(self, texto):
        limpiar = unicodedata.normalize('NFD', texto)
        texto_limpio = ''.join(char for char in limpiar if not unicodedata.combining(char)).lower()
        return texto_limpio
