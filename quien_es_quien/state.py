import reflex as rx
import random
from quien_es_quien import personajes
import unicodedata


# Personaje aleatorio

def escoger_carta(): 
    global elegido   
    elegido = random.choice(personajes.integrantes)
    return personajes.integrantes.index(elegido) + 1

# Enviar el mensaje del input


class State(rx.State):

    pregunta_usuario: str = ""
    pregunta_limpia: str = ""
    cartas_tapadas: list = []
    

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
        self.cartas_tapadas = []
        for personas in personajes.integrantes:
            if self.pregunta_limpia in str(elegido):
                if self.pregunta_limpia not in str(personas):
                    self.cartas_tapadas.append(personajes.integrantes.index(personas) + 1)
            else:
                if self.pregunta_limpia in str(personas):
                    self.cartas_tapadas.append(personajes.integrantes.index(personas) + 1)
                
        return print(self.cartas_tapadas) and self.cartas_tapadas