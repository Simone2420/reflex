import reflex as rx
def nav_bar() -> rx.Component :
    return rx.hstack(
        rx.text(
            "Nombre Empresa",
            color="#E4E4E4",
            class_name=".text",
            
        ),
        rx.hstack(
            rx.link("Inicio", href="#", color="#ffffff"),
            rx.link("Servicios", href="#", color="#ffffff"),
            rx.link("Contacto", href="#", color="#ffffff"),
        ),
        position="sticky",
        display="flex",
        align_items="center",
        gap="auto",
        bg="#066699",
        padding_y="10px",
        padding_x="20px",
        width="100%",
        height="50px",
        z_index="99"
    )
def link_button(text:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(text),
        href=url,
        is_external=True,
        
    )