
import random
from quien_es_quien import personajes



# Personaje aleatorio

def escoger_carta():    

    return random.choice(personajes.integrantes).nombre

