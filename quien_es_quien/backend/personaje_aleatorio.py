import random
from quien_es_quien import personajes

def personaje_aleatorio(state):
    state.elegido = random.choice(personajes.integrantes)
    state.elegido_num = personajes.integrantes.index(state.elegido) + 1