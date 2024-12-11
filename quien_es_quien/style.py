import reflex as rx

menu = dict(
        width="15%",
        height="60vh",
        background_color="pink",
        position="absolute",
        left="0%",
        top="0",
        margin="2rem",
    )
caja_cartas = dict(
        width="50%",
        height="75vh",
        background_color="gray",
        position="absolute",
        left="25%",
        top="0",
        margin="0",
        align = 'center'
    )
caja_texto = dict(
        rx.input(placeholder="Ej: ¿Lleva gafas?", width="100%"),
        width="58%",
        position="absolute",
        left="25%",
        top="80vh",  
        margin="1rem",
)
personaje_misterioso = dict(
        height = "26em",
        width = "15em",
        position="absolute",
        left="82%",
        top="14%",
        margin="2rem",
)