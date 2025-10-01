import reflex as rx

class InputState(rx.State):
    is_focused: bool = False

    def set_focus(self, focused: bool):
        self.is_focused = focused


def input_component(placeholder: str, width: str | None):
    
    return rx.input(
        placeholder=placeholder,
        width=width,
        on_focus=lambda: InputState.set_focus(True),
        on_blur=lambda: InputState.set_focus(False),
        padding="10px",
        height="50px",
        margin_bottom="15px",
        border="1px solid #ccc",
        border_radius="5px",
        font_size="16px",
        class_name="input",
    )
def textarea_component(placeholder: str, width: str | None, height: str | None):
    return rx.input(
        placeholder=placeholder,
        width=width,
        height=height,
        on_focus=lambda: InputState.set_focus(True),
        on_blur=lambda: InputState.set_focus(False),
        padding="10px",
        margin_bottom="15px",
        border="1px solid #ccc",
        border_radius="5px",
        font_size="16px",
        class_name="input",
    )
