"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from fastapi import FastAPI

from campos_omar.components.nav_bar import *
from campos_omar.components.styles import *
from campos_omar.components.section import *
from rxconfig import config

api = FastAPI()

@api.get("/")
def get_data():
    return {"mensaje": "¡Hola desde la API Reflex en el puerto 800!"}


class State(rx.State):
    pass


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        nav_bar(),
        section("Transformando cosechas en alimentos", None, "hero.png"),
        margin="10px",
        
    )
    


app = rx.App(style=style, api_transformer=api)
app.add_page(index)
