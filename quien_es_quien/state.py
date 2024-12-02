import reflex as rx
import random
from quien_es_quien import personajes


# Personaje aleatorio

def escoger_carta():    

    return random.choice(personajes.integrantes).nombre



class State(rx.State):

    pregunta_usuario: str = ""

    @rx.event
    def mensaje_usuario(self):
        
        return print(self.pregunta_usuario)
   

