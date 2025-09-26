import reflex as rx

def product(name: str, image: str) -> rx.Component:
    return rx.vstack(
        rx.image(src=image, alt=name, width="150px", height="150px"),
        rx.text(name, font_size="18px", font_weight="bold", margin_top="10px"),
        border="1px solid #ccc",
        border_radius="10px",
        padding="10px",
        box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
        background_color="#fff",
        align="center",
        width="180px",
    )