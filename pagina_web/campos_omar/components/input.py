import reflex as rx



def input_component(placeholder: str, width: str | None):
    
    return rx.box( 
        # rx.text(placeholder, 
        #         position="absolute", 
        #         position_top="70%",
        #         position_left="20px",
        #         font_size="16px",
        #     ),
        rx.input(
        placeholder= f"{placeholder}",
        width=width,
        
        padding="10px",
        height="50px",
        margin_bottom="15px",
        border="1px solid #ccc",
        border_radius="5px",
        font_size="16px",
        class_name="input",
    ))
def textarea_component(placeholder: str, width: str | None, height: str | None):
    return rx.input(
        placeholder=placeholder,
        width=width,
        height=height,
        padding="10px",
        margin_bottom="15px",
        border="1px solid #ccc",
        border_radius="5px",
        font_size="16px",
        class_name="input",
    )
