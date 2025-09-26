import reflex as rx

def testify_card(rateting: int, comment: str, author: str) -> rx.Component:
    stars = "⭐" * rateting
    return rx.vstack(
        rx.text(stars, font_size="20px"),
        rx.text(f'"{comment}"', font_style="italic", text_align="center"),
        rx.text(f"- {author}", font_weight="bold", margin_top="5px"),
        border="1px solid #ccc",
        border_radius="10px",
        padding="15px",
        box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
        width="300px",
        background_color="#f9f9f9",
    )