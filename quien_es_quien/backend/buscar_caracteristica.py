from quien_es_quien import personajes

def buscar_caracteristica(state): 
    for persona in personajes.integrantes:
        if state.mensaje_limpio in str(state.elegido):
            if state.mensaje_limpio not in str(persona) and personajes.integrantes.index(persona) not in state.cartas_tapadas:
                state.cartas_tapadas.append(personajes.integrantes.index(persona))
        else:
            if state.mensaje_limpio in str(persona) and personajes.integrantes.index(persona) not in state.cartas_tapadas:
                state.cartas_tapadas.append(personajes.integrantes.index(persona))