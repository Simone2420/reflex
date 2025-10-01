import reflex as rx

def form(inputs: list[rx.Component]) -> rx.Component:
    return rx.vstack(
        rx.heading("Contáctanos", font_size="24px", margin_bottom="10px"),
        rx.form(
        *inputs,
        rx.button("Submit", class_name="button"),
        action= "POST",
        width="95%",
        height="auto",

    ),
    padding="20px",
    border="1px solid #ccc",
    border_radius="10px",
    box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
    background_color="#f9f9f9",
    width="400px",
    height="auto",
    min_height="300px",
    align="center",
    justify="center",
    )