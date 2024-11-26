"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config
from quien_es_quien import style


class State(rx.State):
    """The app state."""

    ...


def cartas() -> rx.Component:
    return rx.grid(
        rx.foreach(
            rx.Var.range(24),
            lambda i: rx.card(f"Card {i + 1}", height="20vh"),
        ),
        columns="8",
        spacing="3",
        width="60%",
    )

def index() -> rx.Component:
    return rx.center(
        cartas()
         
    )

app = rx.App()
app.add_page(index)