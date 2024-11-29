
import random
import personajes



# Personaje aleatorio

def escoger_carta():    

    return random.choice(personajes.personajes).nombre


print(escoger_carta())