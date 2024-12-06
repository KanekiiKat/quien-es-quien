
import reflex as rx
from rxconfig import config
from quien_es_quien import style
from quien_es_quien import state
from quien_es_quien.state import State
from quien_es_quien import personajes



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

def pantalla_victoria():
    return rx.dialog.root(
    rx.dialog.trigger(
                rx.cond(
                    State.victoria,
                    
                )
            ),
    rx.dialog.content(
        rx.dialog.title("Welcome to Reflex!"),
        rx.dialog.description(
            "This is a dialog component. You can render anything you want in here.",
        ),
        rx.dialog.close(
            rx.button("Close Dialog", size="3"),
        ),
    ),
)

'''
def pantalla_derrota():
    return rx.dialog(
        is_open=State.derrota,  # Se muestra si derrota es True
        children=[
            rx.dialog.title("¡Te equivocaste!"),
            rx.dialog.description("Haber estudiao."),
            rx.dialog.close(
                rx.button(
                    "Reintentar", size = "3"
                )
            ),
        ],
    )
'''



def barra_de_accion() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.pregunta_usuario,
            placeholder="Ej: ¿Lleva gafas?", 
            width="75%",
            on_change=State.escribir_pregunta_usuario,
        ),
        rx.button(
            "Enviar",
            on_click=State.test
            ),
        style = style.caja_texto,

    )
    
def personaje_a_adivinar() -> rx.Component:
    return rx.box(
        state.escoger_carta(),
        style = style.personaje_misterioso
    )

def index() -> rx.Component:
    return rx.box(
        zona_de_personajes(),
        personaje_a_adivinar(),
        barra_de_accion(),
        pantalla_victoria()
    )

app = rx.App()
app.add_page(index)