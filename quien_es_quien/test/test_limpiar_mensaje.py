import pytest
from quien_es_quien.backend.limpiar_mensaje import limpiar_mensaje
from quien_es_quien.state import State

@pytest.mark.parametrize("mensaje, mensaje_limpio", [
    
    ("", ""),
    ("¿Sombrero?", "sombrero"),
    ("Pelo rubio??", "pelorubio"),
    ("bárbÁ", "barba"),
    ("  Mujer" , "mujer"),
    ("CALVO", "calvo"),
])
def test_limpiar_mensaje(mensaje, mensaje_limpio):
    state = State()
    state.mensaje = mensaje

    limpiar_mensaje(state)

    assert state.mensaje_limpio == mensaje_limpio
