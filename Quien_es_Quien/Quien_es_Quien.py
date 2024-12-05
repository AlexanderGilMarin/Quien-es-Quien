import reflex as rx


personajes = [
    {"nombre": "Susan", "imagen": "Susan.png"},
    {"nombre": "Claire", "imagen": "Claire.png"},
    {"nombre": "David", "imagen": "David.png"},
    {"nombre": "Anne", "imagen": "Anne.png"},
    {"nombre": "Robert", "imagen": "Robert.png"},
    {"nombre": "Anita", "imagen": "Anita.png"},
    {"nombre": "Joe", "imagen": "Joe.png"},
    {"nombre": "George", "imagen": "George.png"},
    {"nombre": "Bill", "imagen": "Bill.png"},
    {"nombre": "Alfred", "imagen": "Alfred.png"},
    {"nombre": "Max", "imagen": "Max.png"},
    {"nombre": "Tom", "imagen": "Tom.png"},
    {"nombre": "Alex", "imagen": "Alex.png"},
    {"nombre": "Sam", "imagen": "Sam.png"},
    {"nombre": "Richard", "imagen": "Richard.png"},
    {"nombre": "Paul", "imagen": "Paul.png"},
    {"nombre": "Maria", "imagen": "Maria.png"},
    {"nombre": "Frans", "imagen": "Frans.png"},
    {"nombre": "Herman", "imagen": "Herman.png"},
    {"nombre": "Bernard", "imagen": "Bernard.png"},
    {"nombre": "Philip", "imagen": "Philip.png"},
    {"nombre": "Eric", "imagen": "Eric.png"},
    {"nombre": "Charles", "imagen": "Charles.png"},
    {"nombre": "Peter", "imagen": "Peter.png"},
]


def tablero():
    filas = []
    
    for i in range(0, len(personajes), 6):
        fila = rx.hstack(
            [
                rx.box(
                    rx.image(src=personaje["imagen"], alt=personaje["nombre"], width="150px", height="150px"),  
                    rx.text(personaje["nombre"], font_size="14px", color="black"),
                    bg="lightblue",
                    p="10px",
                    m="5px",
                    border_radius="8px",
                    text_align="center",
                )
                for personaje in personajes[i:i + 6]
            ],
            spacing="3", 
        )
        filas.append(fila)

    return rx.center(
        rx.vstack(*filas, spacing="3"),  
        padding="20px",
    )


app = rx.App()
app.add_page(tablero, route="/", title="Tablero ¿Quién es quién?")
app._compile()
