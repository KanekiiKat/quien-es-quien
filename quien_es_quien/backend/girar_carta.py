
def girar_carta(state):
    for carta in state.cartas_tapadas:
        state.show[carta] = False