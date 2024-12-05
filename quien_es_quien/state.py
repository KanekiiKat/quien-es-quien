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
    show: list = [True] * 24
    cartas_tapadas: list = []
    cartas_a_tapar: list = []


    def change(self):
        for carta in self.cartas_tapadas: 
            self.show[carta] = False




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


    def identificar_caracteristicas(self): 
        if self.pregunta_limpia == "reset":
            self.show = [True] * 24
            self.cartas_tapadas = []
        for persona in personajes.integrantes:
            if self.pregunta_limpia in str(elegido):
                if self.pregunta_limpia not in str(persona) and personajes.integrantes.index(persona) not in self.cartas_tapadas:
                    self.cartas_tapadas.append(personajes.integrantes.index(persona))
            else:
                if self.pregunta_limpia in str(persona) and personajes.integrantes.index(persona) not in self.cartas_tapadas:
                    self.cartas_tapadas.append(personajes.integrantes.index(persona))
        self.change()
        print(self.cartas_tapadas)