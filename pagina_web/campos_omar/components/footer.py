import reflex as rx

def footer(opciones: list[rx.Component]) -> rx.Component:
    return rx.vstack(
        rx.image(src="/logo.svg"),
        rx.link("Github", href="https://github.com/Simone2420/reflex", is_external=True),
        rx.hstack(
            *opciones,
            gap="20px"
        ),
        align="start"
        

    )