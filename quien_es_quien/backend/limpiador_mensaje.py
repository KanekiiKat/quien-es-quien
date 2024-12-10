import unicodedata
# from state import State 

def limpia_mensaje(state):
    if state.mensaje:
        state.mensaje_limpio = ''.join(char for char in unicodedata.normalize('NFD', state.mensaje) if not unicodedata.combining(char)).lower()
        state.mensaje = ""
        state.analizar_mensaje()