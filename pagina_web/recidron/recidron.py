"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from recidron.components.nav_bar import *
from rxconfig import config


class State(rx.State):
    pass


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        nav_bar(),
        link_button("Ingreso","https://reflex.dev/docs/library/"),
        margin="30px",
    )
    


app = rx.App()
app.add_page(index)
