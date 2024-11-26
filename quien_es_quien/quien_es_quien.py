"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.box(
        "CSS color",
        background_color="orange",
        border_radius="5px",
        width="40%",
        margin="8px",
        padding="8px",
    ),
    )


app = rx.App()
app.add_page(index)
