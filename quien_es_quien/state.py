import reflex as rx
import random
from quien_es_quien import personajes
import unicodedata

'''
def escoger_carta():
    global elegido
    elegido = random.choice(personajes.integrantes)
    global elegido_num
    elegido_num = personajes.integrantes.index(elegido) + 1
    print(elegido_num)
    return elegido_num
'''
class State(rx.State):

    pregunta_usuario: str = ""
    pregunta_limpia: str = ""
    show: list = [True] * 24
    cartas_tapadas: list = []
    cartas_a_tapar: list = []
    fin_de_juego: bool = False
    elegido = ""
    elegido_num = ""

    def escoger_carta(self):
        self.elegido = random.choice(personajes.integrantes)
        self.elegido_num = personajes.integrantes.index(self.elegido) + 1
        print(self.elegido_num)
        

    
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


    def adivinar(self):
        for persona in personajes.integrantes:
            if self.pregunta_limpia in persona.nombre:
                if self.pregunta_limpia == self.elegido.nombre:
                    self.fin_de_juego = True
                    return rx.toast.success("¡Has ganado!")
                elif self.pregunta_limpia != self.elegido.nombre:
                    self.fin_de_juego = True
                    return rx.toast.success("Das pena XD")


    def identificar_caracteristicas(self):
        if self.pregunta_limpia == "reset":
            self.show = [True] * 24
            self.cartas_tapadas = []
            self.fin_de_juego = False
            self.escoger_carta()
        for persona in personajes.integrantes:
            if self.pregunta_limpia in str(self.elegido):
                if self.pregunta_limpia not in str(persona) and personajes.integrantes.index(persona) not in self.cartas_tapadas:
                    self.cartas_tapadas.append(personajes.integrantes.index(persona))
            else:
                if self.pregunta_limpia in str(persona) and personajes.integrantes.index(persona) not in self.cartas_tapadas:
                    self.cartas_tapadas.append(personajes.integrantes.index(persona))
        self.change()
        print(self.cartas_tapadas)

    def test(self):
        self.mensaje_usuario()
        self.adivinar()