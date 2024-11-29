
import reflex as rx
from rxconfig import config
from quien_es_quien import style
from quien_es_quien import state

def bloque_cartas() -> rx.Component:
    return rx.center(
        rx.box(
            style = style.caja_cartas,
    )
    )
    
def menu() -> rx.Component:
    return rx.box(
        style = style.menu,
    )
    
def caja_texto() -> rx.Component:
    return rx.box(
        rx.input(placeholder="Ej: ¿Lleva gafas?", width="75%",),
        rx.button("Enviar"),
        style=style.caja_texto,
    )

    
def personaje_a_adivinar() -> rx.Component:
    return rx.box(
        state.escoger_carta(),
        style = style.personaje_misterioso
    )
    
def index() -> rx.Component:
    return rx.box(
        menu(),
        bloque_cartas(),
        personaje_a_adivinar(),
        caja_texto(),
    )

app = rx.App()
app.add_page(index)