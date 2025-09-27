import reflex as rx



def nav_bar() -> rx.Component :
    return rx.hstack(
        rx.hstack(
        rx.image(src="/logo.svg"),
        rx.text(
            "Campos Omar",
            color="#000000",
            class_name=".text",
            font_size="40px",
            
        ),
        align_items="center",
        ),
        rx.hstack(
            rx.link("Inicio", href="#", color="#000000", class_name="link"),
            rx.link("Productos", href="#", color="#000000", class_name="link"),
            rx.link("Galeria", href="#", color="#000000", class_name="link"),
            rx.link("Testimonios", href="#", color="#000000", class_name="link"),
            rx.link("Contactenos", href="#", color="#000000", class_name="link"),
            link_button(None,"Ingreso","https://reflex.dev/docs/library/"),
            align_items="center",
        ),
        position="fixed",
        display="flex",
        align_items="center",
        justify_content="space-evenly",
        bg="#DDFFDC",
        padding_y="10px",
        padding_x="20px",
        width="100%",
        height="50px",
        z_index="9"
    )
def link_button(icon: str | None, text:str, url:str) -> rx.Component:
    return rx.link(
        
        rx.button(rx.image(src=icon) if icon else None, text, class_name="button"),
        href=url,
        is_external=True,
        
    )