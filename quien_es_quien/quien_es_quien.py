
import reflex as rx
from rxconfig import config
from quien_es_quien import style
from quien_es_quien import state
from quien_es_quien import personajes

lista = ['Alex', 'Alfred', 'Anita', 'Anne', 'Bernard', 'Bill', 'Charles', 'Claire', 'David', 'Eric', 'Frans', 'George', 'Herman', 'Joe', 'Maria', 'Max', 'Paul', 'Peter', 'Philip', 'Richard', 'Robert', 'Sam', 'Susan', 'Tom']

def zona_de_personajes() -> rx.Component:
    return rx.center(
        rx.grid(
            rx.foreach(
                rx.Var.range(24), lambda i:
                    rx.card(
                        rx.image(
                            src=f"{lista[i + 1]}.jpg", width="100%", height="50%"
                        ),
                        height="13em",
                        width="7.5em"
                ),
            ),
            columns="8",
            spacing="4",
            width="60%",
        )
    )

def barra_de_accion() -> rx.Component:
    return rx.hstack(

        rx.input(placeholder="Ej: ¿Lleva gafas?", width="75%",),
        rx.button("Enviar"),
        style=style.caja_texto,
        left="28%",
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
    )

app = rx.App()
app.add_page(index)