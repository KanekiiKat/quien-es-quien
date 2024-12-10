import pytest
from quien_es_quien.backend.buscar_caracteristica import buscar_caracteristica
from quien_es_quien.state import State
from quien_es_quien import personajes

@pytest.mark.parametrize("mensaje_limpio, elegido, cartas_tapadas",[
    ("rubio", 1, [2, 6, 8, 9, 13]),
    ("calvo", 1 , [5, 12, 19, 21, 23]),
    ("blanco", 15, [11, 16, 17, 22]),
    ("", 1, []),
    ("hombre", 2, [0, 1, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 23]),
])
def test_buscar_caracteristica(mensaje_limpio, elegido, cartas_tapadas):
    state = State()
    state.mensaje_limpio = mensaje_limpio
    state.elegido = elegido

    buscar_caracteristica(state)

    assert state.cartas_tapadas == cartas_tapadas

