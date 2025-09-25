import reflex as rx
style = {
    # Set the selection highlight color globally.
    "::selection": {
        "background_color": "#5BFFDB",
    },
    # Apply global css class styles.
    ".text:hover": {
        "text_decoration": "underline",
    },
    # Apply global css id styles.
    "#special-input": {"width": "20vw"},
    # Apply styles to specific components.
    rx.text: {
        "font_family": "Comic Sans MS",
        
       
    },
    rx.divider: {
        "margin_bottom": "1em",
        "margin_top": "0.5em",
    },
    rx.heading: {
        "font_weight": "500",
        "color": "blue",
        "transform": "rotate(10deg) translate(100px, 50px)",
        "transform_origin": f"75% 200%",
        "animation_name": "colorchange",
        "animation_duration": "2s",
        "animation_iteration_count": "infinite",
    },
    rx.code: {
        "color": "green",
    },
    "@keyframes colorchange": {
        "from": {"color": "red"},
        "to": {"color": "green"}
}
}


