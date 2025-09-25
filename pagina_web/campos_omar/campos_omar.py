"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from campos_omar.components.nav_bar import *
from campos_omar.components.styles import *
from rxconfig import config


class State(rx.State):
    pass


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        nav_bar(),
        rx.heading("Hola"),
        rx.text("Hola 2", class_name="text",),
        link_button("Ingreso","https://reflex.dev/docs/library/"),
        margin="30px",
    )
    


app = rx.App(style=style)
app.add_page(index)
