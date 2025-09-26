import reflex as rx

def input_component(placeholder: str, width: str | None) -> rx.Component:
    return rx.input(
        placeholder=placeholder,
        width=width,
        padding="10px",
        border="1px solid #ccc",
        border_radius="5px",
        font_size="16px",
    )