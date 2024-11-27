
import reflex as rx
from rxconfig import config
from quien_es_quien import style

def bloque_cartas() -> rx.Component:
    return rx.center(
            rx.box(
            width="50%",
            height="75vh",
            background_color="gray",
            position="absolute",
            left="25%",
            top="0",
            margin="0",
            align = 'center'
    )
    )

def menu() -> rx.Component:
    return rx.box(
        width="15%",
        height="60vh",
        background_color="pink",
        position="absolute",
        left="0%",
        top="0",
        margin="2rem",
    )

def caja_input() -> rx.Component:
    return rx.box(
        rx.input(placeholder="Ej: ¿Lleva gafas?", width="100%"),
        width="50%",
        position="absolute",
        left="25%",
        top="80vh",  
        margin="1rem",
    )

def personaje_a_adivinar() -> rx.Component:
    return rx.box(
        "Pedro",
        width="15%",
        height="35vh",
        background_color="red",
        position="absolute",
        left="80%",
        top="18%",
        margin="2rem",
    )

def index() -> rx.Component:
    return rx.box(
        menu(),
        bloque_cartas(),
        personaje_a_adivinar(),
        caja_input(),
    )

app = rx.App()
app.add_page(index)