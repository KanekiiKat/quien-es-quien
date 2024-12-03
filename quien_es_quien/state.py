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
    pregunta_limpia: str = ""

    @rx.event
    def escribir_pregunta_usuario(self, value):
        self.pregunta_usuario = value

    def limpiar_palabra(self, texto):
        texto_limpio = ''.join(char for char in unicodedata.normalize('NFD', texto) if not unicodedata.combining(char)).lower()
        return texto_limpio

    

    def mensaje_usuario(self):
        
        if self.pregunta_usuario:
            self.pregunta_limpia = self.limpiar_palabra(self.pregunta_usuario)
            self.pregunta_usuario = ""
            self.identificar_caracteristicas()
            print(self.pregunta_limpia)
         

    def identificar_caracteristicas(self):
        for personas in personajes.integrantes:

            if self.pregunta_limpia in str(personas):
                print(f"{personas.nombre}")