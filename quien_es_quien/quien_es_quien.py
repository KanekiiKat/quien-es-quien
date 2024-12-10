
import reflex as rx
from rxconfig import config
from quien_es_quien import style
from quien_es_quien import state
from quien_es_quien.state import State

def zona_de_personajes() -> rx.Component:
    return rx.center(
        rx.grid(
            rx.foreach(
                rx.Var.range(24), lambda i:
                    rx.card(
                        rx.inset(
                            rx.cond(
                                State.show[i],
                                rx.image(
                                    src=f"{i + 1}.jpg", width = "100%", height = "100%"
                                ),
                                
                                rx.image(
                                    src="cartatapada.jpg", width = "100%", height = "100%"
                                ),
                                

                            ),
                            height = "13em",
                            width = "7.5em"
                        ),
                        id=f"{i+1}"
                    ),
                ),
                columns="8",
                spacing="4",
                width="60%",
            ),
            
        ),


def barra_de_accion() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.mensaje,
            placeholder="Ej: Gafas", 
            width="75%",
            on_change=State.detectar_mensaje,
        ),
        rx.button(
            "Enviar",
            on_click=[State.analizar_mensaje, State.adivinar]
            ),
        style = style.caja_texto,

    )
    
def personaje_a_adivinar() -> rx.Component:
    return rx.box(
        rx.cond(
            State.fin_de_juego,
            rx.image(src= State.elegido_num + ".jpg", width="100%", heigth="100%",
                     ),
                     
            rx.image(src="cartatapada.jpg", width="100%", heigth="100%",
                     ),
        ),
        style = style.personaje_misterioso
    )
@rx.page(on_load=State.personaje_aleatorio)
def index() -> rx.Component:
    return rx.box(
        zona_de_personajes(),
        personaje_a_adivinar(),
        barra_de_accion(),
    )
 
app = rx.App()
app.add_page(index)