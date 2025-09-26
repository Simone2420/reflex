import reflex as rx

def image_component(src: str, alt: str, width: str, height: str) -> rx.Component:
    return rx.image(
        src=src,
        alt=alt,
        width=width,
        height=height,
    )