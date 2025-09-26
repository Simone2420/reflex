import reflex as rx

def section(title: str, content: str | None, background_image: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, 
                   font_size="24px", 
                   margin_bottom="10px",
                   color="#ffffff",
                   width="400px", 
                   text_align="center"
                   ),
        rx.text(content, font_size="16px") if content else None,
        rx.hstack(
            rx.button("Ver Productos", class_name="button"),
            rx.button("Contactenos", class_name="button"),
        ),
        background_image=f"url({background_image})",
        width="100%",
        padding="20px",
        height="auto",
        min_height="300px",
        align="center",
        justify="center",
    )