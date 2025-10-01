"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from campos_omar.components.nav_bar import *
from campos_omar.components.styles import *
from campos_omar.components.section import *
from campos_omar.components.product import *
from campos_omar.components.gallery_card import *
from campos_omar.components.testify_card import *
from campos_omar.components.ratings import *
from campos_omar.components.form import *
from campos_omar.components.input import *
from campos_omar.components.footer import *
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
        general_section(
            section_title("Sobre Nosostros"),
            section_content(
                "Campos Omar",
                content([
                    rx.text("En Campos Omar creemos que la alimentación es un puente entre el campo y la ciudad. Nacimos con la idea de dar valor a las cosechas locales, transformándolas en productos orgánicos y sostenibles que llegan frescos a tu mesa. Nuestro compromiso es con la salud de las personas, el cuidado del planeta y el bienestar de los agricultores que hacen posible cada alimento.", width="100%"),
                    rx.text("Trabajamos de la mano con agricultores locales, apoyando prácticas de cultivo responsables y comercio justo. Cada producto que elaboramos cuenta una historia de respeto por la tierra y por quienes la trabajan. Nuestra fábrica no solo transforma alimentos, también transforma realidades, ofreciendo opciones saludables a los consumidores y creando un futuro más sostenible para todos", width="100%")

                ]),
            ),
            "main.png"
        ),
        general_section(
            section_title("Productos"),
            horizontal_content([
                product("Jugos Naturales", "/products_assets/jugo.png"),
                product("Snacks", "/products_assets/galletas.png"),
                product("Harinas", "/products_assets/harina.png"),
                product("Conservas", "/products_assets/mermelada.png"),
                product("Aceites", "/products_assets/aceite.png"),
                product("Condimentos", "/products_assets/comino.png"),
                product("Super Alimentos", "/products_assets/cacao.png"),

            ]),
            None
        ), 
        general_section(
            section_title("Galería"),
            content([
                horizontal_content([
                    gallery_card("/gallery_assets/jugos_naturales.png", "Jugos Naturales"),
                    gallery_card("/gallery_assets/galletas_saludables.png", "Galletas Saludables"),
                    gallery_card("/gallery_assets/mermeladas_naturales.png", "Mermeladas Naturales"),

                ]),
                horizontal_content([
                    gallery_card("/gallery_assets/harinas_integrales.png", "Harinas Integrales"),
                    gallery_card("/gallery_assets/aceites_saludables.png", "Aceites Saludables"),
                    gallery_card("/gallery_assets/condimentos.png", "Condimentos"),

                ]),
            ]),
            None
            ),
        general_section(
            section_title("Testimonios"),
            horizontal_content([
                testify_card(
                    rating(5), 
                    "Los productos son de excepcional calidad",
                    "Carlos Inti", 
                    "Cliente", 
                    "12/03/2023"
                    ),
                testify_card(
                    rating(5), 
                    "Las comisiones recibidas son justas",
                    "Blass Muñoz", 
                    "Agricultor", 
                    "12/03/2023"
                    ),
                testify_card(
                    rating(4), 
                    "Los productos son naturales y deliciosos",
                    "Nicolas Herrera", 
                    "Cliente", 
                    "12/03/2023"
                    ),
            ], gap="60px"),
            None),
            general_section(
            section_title("Contáctanos"),
            horizontal_content([
                section_content("Campos Omar", section_content(
                    "Contactate con el area de mercadeo",
                    content([
                        rx.text("Descubre cómo nuestros productos orgánicos pueden transformar tu alimentación y contribuir a un futuro más saludable y sostenible. Completa el formulario y nos pondremos en contacto contigo muy pronto.")
                    ]))
                ),
                form([
                    input_component("Nombre", "300px"),
                    input_component("Correo Electrónico", "300px"),
                    textarea_component("Escribe tu mensaje aquí...", "300px", "100px")
                ])

            ]),
            None
        ),
        footer([
            rx.link("Nosostros"),
            rx.link("Producto"),
            rx.link("Galeria"),
            rx.link("Testimonios"),
            rx.link("Contacto")
        ])
        )


app = rx.App(style=style, api_transformer=api)
app.add_page(index)
