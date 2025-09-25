import reflex as rx

config = rx.Config(
    app_name="campos_omar",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)