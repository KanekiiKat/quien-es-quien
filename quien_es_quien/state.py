import reflex as rx
import random
from quien_es_quien import personajes
from quien_es_quien.backend.limpiar_mensaje import limpiar_mensaje
from quien_es_quien.backend.girar_carta import girar_carta
class State(rx.State):

    mensaje: str = ""
    mensaje_limpio: str = ""
    show: list = [True] * 24
    cartas_tapadas: list = []
    cartas_a_tapar: list = []
    fin_de_juego: bool = False
    elegido = ""
    elegido_num = ""

    def escoger_personaje(self):
        self.elegido = random.choice(personajes.integrantes)
        self.elegido_num = personajes.integrantes.index(self.elegido) + 1
    
    def girar_carta(self):
        girar_carta(self)


    def detectar_mensaje(self, value):
        self.mensaje = value


    def limpiar_mensaje(self):
        limpiar_mensaje(self)


    def adivinar(self):
        for persona in personajes.integrantes:
            if self.mensaje_limpio in persona.nombre:
                if self.mensaje_limpio == self.elegido.nombre:
                    self.fin_de_juego = True
                    return rx.toast.success("¡Has ganado!")
                elif self.mensaje_limpio != self.elegido.nombre:
                    self.fin_de_juego = True
                    return rx.toast.success("Das pena XD")


    def analizar_mensaje(self):
        if self.mensaje_limpio == "reset":
            self.show = [True] * 24
            self.cartas_tapadas = []
            self.fin_de_juego = False
            self.escoger_personaje()
        for persona in personajes.integrantes:
            if self.mensaje_limpio in str(self.elegido):
                if self.mensaje_limpio not in str(persona) and personajes.integrantes.index(persona) not in self.cartas_tapadas:
                    self.cartas_tapadas.append(personajes.integrantes.index(persona))
            else:
                if self.mensaje_limpio in str(persona) and personajes.integrantes.index(persona) not in self.cartas_tapadas:
                    self.cartas_tapadas.append(personajes.integrantes.index(persona))
        self.girar_carta()

    def test(self):
        self.limpiar_mensaje()
        self.adivinar()