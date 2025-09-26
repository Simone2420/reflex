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
        "font_family": "Roboto",
        
    },
    rx.divider: {
        "margin_bottom": "1em",
        "margin_top": "0.5em",
    },
    rx.heading: {
        "font_weight": "500",
        "color": "blue",
        "transform": "rotate(10deg) translate(100px)",
        #"transform_origin": f"75% 200%",
        "animation_name": "colorchange, slide-in",
        "animation_duration": "2s , 3s",
        "animation_iteration_count": "infinite , 1",
        "animation_direction": "alternate , normal",
        "animation_timing_function": "ease-in-out , ease-in-out",
    },
    rx.code: {
        "color": "green",
    },
    rx.link: {
        "text_decoration": "none",
        "color": "blue",
    },
    rx.button: {
        "background_color": "#33FF4E",
    },
    ".button:hover": {
        "background_color": "#28CC3E",
    },
    ".link:hover": {
        "text_decoration": "none",
        "color": "#33FF4E",
    },
    "@keyframes colorchange": {
        "from": {"color": "red"},
        "to": {"color": "green"}
    },
    "@keyframes slide-in": {
        "from": {"transform": "translateX(-100%)"},
        "to": {"transform": "translateX(0)"}
    }
}


