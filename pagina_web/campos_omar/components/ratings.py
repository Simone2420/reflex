import reflex as rx

def rating(stars: int) -> rx.Component:
    return rx.hstack(
        *[rx.image(src="star.png" if i < stars else "star_border.png") for i in range(5)],
        gap="2px",
    )