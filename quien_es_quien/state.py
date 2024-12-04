import reflex as rx
import random
from quien_es_quien import personajes
import unicodedata


def escoger_carta(): 
    global elegido   
    elegido = random.choice(personajes.integrantes)
    return personajes.integrantes.index(elegido) + 1


class State(rx.State):

    pregunta_usuario: str = ""
    pregunta_limpia: str = ""
    cartas_tapadas: list = []
    show: bool = True

    
    def change(self):
        self.show = not (self.show) 

    def escribir_pregunta_usuario(self, value):
        self.pregunta_usuario = value


    def limpiar_palabra(self, texto):

        texto_limpio = ''.join(char for char in unicodedata.normalize('NFD', texto) if not unicodedata.combining(char)).lower()
        return texto_limpio


    def mensaje_usuario(self):
        self.change()
        if self.pregunta_usuario:
            self.pregunta_limpia = self.limpiar_palabra(self.pregunta_usuario)
            self.pregunta_usuario = ""
            self.identificar_caracteristicas()    


    def identificar_caracteristicas(self):
        self.cartas_tapadas = []

        for personas in personajes.integrantes:
            if self.pregunta_limpia in str(elegido):
                if self.pregunta_limpia not in str(personas):
                    self.cartas_tapadas.append(personajes.integrantes.index(personas) + 1)
                    
            else:
                if self.pregunta_limpia in str(personas):
                    self.cartas_tapadas.append(personajes.integrantes.index(personas) + 1)

        return self.cartas_tapadas and print(self.cartas_tapadas)