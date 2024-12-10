def reiniciar(state):
    if state.mensaje_limpio == "reiniciar":
        state.show = [True] * 24
        state.cartas_tapadas = []
        state.fin_de_juego = False
        state.personaje_aleatorio()