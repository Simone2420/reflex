import reflex as rx

def form(inputs: list[rx.Component]) -> rx.Component:
    return rx.vstack(
        *inputs,
        rx.button("Submit", class_name="button"),
        spacing="15px",
        padding="20px",
        border="1px solid #ccc",
        border_radius="10px",
        box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
        background_color="#f9f9f9",
        width="400px",
        align="center",
    ) 