import reflex as rx
import random

personajes = {
    "Susan": {
        "nombre": "Susan",
        "características": ["Pelo", "Ojos Marrones", "Coloretes", "Mujer", "Pelo Blanco"],
        "imagen": "Susan.png",  
    },
    "Claire": {
        "nombre": "Claire",
        "características": ["Pelo", "Sombrero", "Ojos Marrones", "Gafas", "Mujer", "Pelo Naranja"],
        "imagen": "Claire.png",
    },
    "David": {
        "nombre": "David",
        "características": ["Pelo", "Ojos Marrones", "Barba", "Hombre", "Rubio"],
        "imagen": "David.png",
    },
    "Anne": {
        "nombre": "Anne",
        "características": ["Pelo", "Ojos Marrones", "Pendientes", "Mujer", "Pelo Marrón"],
        "imagen": "Anne.png",
    },
    "Robert": {
        "nombre": "Robert",
        "características": ["Pelo", "Ojos Azules", "Coloretes", "Hombre", "Pelo Marrón"],
        "imagen": "Robert.png",
    },
    "Anita": {
        "nombre": "Anita",
        "características": ["Pelo", "Ojos Azules", "Coloretes", "Mujer", "Rubio"],
        "imagen": "Anita.png",
    },
    "Joe": {
        "nombre": "Joe",
        "características": ["Pelo", "Ojos Marrones", "Gafas", "Hombre", "Rubio"],
        "imagen": "Joe.png",
    },
    "George": {
        "nombre": "George",
        "características": ["Pelo", "Sombrero", "Ojos Marrones", "Hombre", "Pelo Blanco"],
        "imagen": "George.png",
    },
    "Bill": {
        "nombre": "Bill",
        "características": ["Calvo", "Ojos Marrones", "Coloretes", "Barba", "Hombre"],
        "imagen": "Bill.png",
    },
    "Alfred": {
        "nombre": "Alfred",
        "características": ["Pelo", "Ojos Azules", "Bigote", "Hombre", "Pelo Naranja"],
        "imagen": "Alfred.png",
    },
    "Max": {
        "nombre": "Max",
        "características": ["Pelo", "Ojos Marrones", "Bigote", "Hombre", "Pelo Marrón"],
        "imagen": "Max.png",
    },
    "Tom": {
        "nombre": "Tom",
        "características": ["Calvo", "Ojos Azules", "Gafas", "Hombre"],
        "imagen": "Tom.png",
    },
    "Alex": {
        "nombre": "Alex",
        "características": ["Pelo", "Ojos Marrones", "Bigote", "Hombre", "Pelo Marrón"],
        "imagen": "Alex.png",
    },
    "Sam": {
        "nombre": "Sam",
        "características": ["Calvo", "Ojos Marrones", "Gafas", "Hombre"],
        "imagen": "Sam.png",
    },
    "Richard": {
        "nombre": "Richard",
        "características": ["Calvo", "Ojos Marrones", "Bigote", "Barba", "Hombre"],
        "imagen": "Richard.png",
    },
    "Paul": {
        "nombre": "Paul",
        "características": ["Pelo", "Ojos Marrones", "Gafas", "Hombre", "Pelo Blanco"],
        "imagen": "Paul.png",
    },
    "Maria": {
        "nombre": "Maria",
        "características": ["Pelo", "Sombrero", "Ojos Marrones", "Pendientes", "Mujer", "Pelo Marrón"],
        "imagen": "Maria.png",
    },
    "Frans": {
        "nombre": "Frans",
        "características": ["Pelo", "Ojos Marrones", "Hombre", "Pelo Naranja"],
        "imagen": "Frans.png",
    },
    "Herman": {
        "nombre": "Herman",
        "características": ["Calvo", "Ojos Marrones", "Hombre"],
        "imagen": "Herman.png",
    },
    "Bernard": {
        "nombre": "Bernard",
        "características": ["Pelo", "Sombrero", "Ojos Marrones", "Hombre", "Pelo Marrón"],
        "imagen": "Bernard.png",
    },
    "Philip": {
        "nombre": "Philip",
        "características": ["Pelo", "Ojos Marrones", "Coloretes", "Barba", "Hombre", "Pelo Marrón"],
        "imagen": "Philip.png",
    },
    "Eric": {
        "nombre": "Eric",
        "características": ["Pelo", "Sombrero", "Ojos Marrones", "Hombre", "Pelo Rubio"],
        "imagen": "Eric.png",
    },
    "Charles": {
        "nombre": "Charles",
        "características": ["Pelo", "Ojos Marrones", "Bigote", "Hombre", "Rubio"],
        "imagen": "Charles.png",
    },
    "Peter": {
        "nombre": "Peter",
        "características": ["Pelo", "Ojos Azules", "Hombre", "Pelo Blanco"],
        "imagen": "Peter.png",
    },
}


def escoger_personaje(personajes):
    personaje_oculto = random.choice(list(personajes.keys()))
    return personaje_oculto


def tablero():
    personajes_lista = list(personajes.values())
    
    filas = []
    
    for i in range(0, len(personajes_lista), 6):  
        fila = rx.hstack(
            [
                rx.box(
                    rx.image(src=personaje["imagen"], alt=personaje["nombre"], width="150px", height="150px"),  
                    rx.text(personaje["nombre"], font_size="14px", color="black"),
                    bg="LightGreen", 
                    p="10px", 
                    m="5px", 
                    border_radius="8px", 
                    text_align="center",
                )
                for personaje in personajes_lista[i:i + 6]  
            ],
            spacing="3", 
        )
        filas.append(fila)
    

    personaje_aleatorio = escoger_personaje(personajes)
    personaje_oculto = personajes[personaje_aleatorio]
    
    return rx.center(
        rx.vstack(
            *filas, 
            rx.text(f"El personaje elegido por la máquina es: {personaje_oculto['nombre']}", font_size="18px", color="blue"),
            rx.image(src=personaje_oculto["imagen"], alt=personaje_oculto["nombre"], width="150px", height="150px"),
            spacing="3",
        ),
        padding="20px",
    )


class Estado(rx.State):
    def mostrar_mensaje(self, mensaje):
        print(f"Has seleccionado a {mensaje}")  


app = rx.App(state=Estado)  
app.add_page(tablero, route="/", title="Tablero ¿Quién es quién?")
app._compile()