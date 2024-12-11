import pytest
from quien_es_quien.backend.buscar_caracteristica import buscar_caracteristica
from quien_es_quien.state import State

@pytest.mark.parametrize("mensaje_limpio, cartas_tapadas",[
    ("", []),
    ("sombrero", [4, 7, 9, 11, 14]),
    ("pelorubio", [2, 6, 8, 9, 13]),
    ("barba", [1, 5, 8, 18, 19]),
    ("mujer" , [0, 1, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 23]),
    ("calvo", [5, 12, 19, 21, 23]),

])
def test_buscar_caracteristica(mensaje_limpio, cartas_tapadas):
    state = State()
    state.mensaje_limpio = mensaje_limpio
    state.elegido = ['negro', 'oscuro', 'pendientes', 'marrones', 'cafe', 'femenino', 'mujer', 'aretes', 'seria', 'formal', 'pelocorto', 'narizgrande'] # Anne
    state.cartas_tapadas = []
    
    buscar_caracteristica(state)

    assert state.cartas_tapadas == cartas_tapadas

