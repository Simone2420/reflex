import reflex as rx

def testify_card(rating: rx.Component, comment: str, author: str, role: str, date: str) -> rx.Component:
    return rx.vstack(
        rating,
        rx.text(f"({role})", font_style="italic", text_align="center"),
        rx.text(f'"{comment}"', font_style="italic", text_align="center"),
        rx.hstack(
            rx.image(src="avatar.png", ),
            rx.vstack(
                rx.text(f"{author}", font_weight="bold", margin_top="5px"),
                rx.text(f"{date}", font_style="italic"),
            ),
        ),
        border="1px solid #ccc",
        border_radius="10px",
        padding="15px",
        box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
        width="330px",
        background_color="#f9f9f9",
    )