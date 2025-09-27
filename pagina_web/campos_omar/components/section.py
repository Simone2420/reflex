import reflex as rx

def section(title: str, content: str | None, background_image: str | None) -> rx.Component:
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

def general_section(section_title: rx.Component, section_content: rx.Component, section_image: str | None) -> rx.Component:
    return rx.vstack(
        section_title,
        rx.hstack(
            rx.image(src=section_image) if section_image else None,
            section_content,
            width="100%",
            height="auto",
        ),
        width="100%",
        padding="40px",
        align="center",
        justify="center",
    )

def section_content(title: str | None, content: rx.Component) -> rx.Component:
    return rx.vstack(
        rx.heading(title, font_size="32px", margin_bottom="10px") if title else None,
        content,
        width="100%",
        height="auto",
        
    )

def content(content: list[rx.Component]) -> rx.Component:
    return rx.vstack(
        *content,
        width="100%",
        height="auto",
        
    )
def horizontal_content(content: list[rx.Component]) -> rx.Component:
    return rx.hstack(
        *content,
        width="100%",
        height="auto",
        gap="auto",
        justify="center",
        align="center",
    )
def section_title(title: str) -> rx.Component:
    return rx.vstack(
        rx.heading(title, font_size="24px", text_decoration="underline"),

    )