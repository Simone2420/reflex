import reflex as rx

class InputState(rx.State):
    is_focused: bool = False
    def toggle_focus(self):
        self.is_focused = not self.is_focused
        self.animate_focus()
    def animate_focus(self):
        return rx.set_state(
            is_focused=self.is_focused,
            placeholder_style={"transform": "translateY(-8px)", "font_size": "14px"} if self.is_focused else {}
        )
def input_component(placeholder: str, width: str | None) -> rx.Component:
    return rx.input(
        placeholder=placeholder,
        width=width,
        on_focus=InputState.toggle_focus,
        padding="10px",
        border="1px solid #ccc",
        border_radius="5px",
        font_size="16px",
    )