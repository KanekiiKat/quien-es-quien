
import reflex as rx
from quien_es_quien import personajes
from quien_es_quien.backend.limpiar_mensaje import limpiar_mensaje
from quien_es_quien.backend.girar_carta import girar_carta
from quien_es_quien.backend.personaje_aleatorio import personaje_aleatorio
from quien_es_quien.backend.reiniciar import reiniciar
from quien_es_quien.backend.buscar_caracteristica import buscar_caracteristica
class State(rx.State):

    mensaje: str = ""
    mensaje_limpio: str = ""
    show: list = [True] * 24
    cartas_tapadas: list = []
    cartas_a_tapar: list = []
    fin_de_juego: bool = False
    elegido = ""
    elegido_num = ""

    def personaje_aleatorio(self):
        personaje_aleatorio(self)
    
    def girar_carta(self):
        girar_carta(self)

    def limpiar_mensaje(self):
        limpiar_mensaje(self)

    def reiniciar(self):
        reiniciar(self)

    def buscar_caracteristica(self):
        buscar_caracteristica(self)

    def detectar_mensaje(self, value):
        self.mensaje = value

    def analizar_mensaje(self):
        self.limpiar_mensaje()
        self.reiniciar()
        self.buscar_caracteristica()
        self.girar_carta()

    def adivinar(self):
        for persona in personajes.integrantes:
            if self.mensaje_limpio in persona.nombre:
                if self.mensaje_limpio == self.elegido.nombre:
                    self.fin_de_juego = True
                    self.girar_carta()
                    return rx.toast.success("¡Has ganado!")
                elif self.mensaje_limpio != self.elegido.nombre:
                    self.fin_de_juego = True
                    self.girar_carta()
                    return rx.toast.success("Das pena XD")

