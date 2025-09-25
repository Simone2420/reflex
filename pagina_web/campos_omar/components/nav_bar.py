import reflex as rx
def nav_bar() -> rx.Component :
    return rx.hstack(
        rx.text(
            "Nombre Empresa",
            color="#AEDD2B",
            class_name=".text",
            
        ),
        position="sticky",
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