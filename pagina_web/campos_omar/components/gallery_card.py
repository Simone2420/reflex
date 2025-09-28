import reflex as rx

def gallery_card(image: str, title: str) -> rx.Component:
    return rx.vstack(
        rx.image(src=image),
        rx.text(title),
        width="100%", 
        align_items="center", 
        justify_content="center"

    )