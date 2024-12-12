import unicodedata

def limpiar_mensaje(state):
    if state.mensaje:
        state.mensaje_limpio = ''.join(caracter for caracter in unicodedata.normalize('NFD', state.mensaje) if not unicodedata.combining(caracter) and caracter.isalpha()).lower()
        state.mensaje = ""
        state.analizar_mensaje()