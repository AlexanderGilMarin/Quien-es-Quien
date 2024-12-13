import pytest
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

class EstadoJuego():
    pregunta: str = ""
    historial_chat: list[tuple[str, str]] = []
    personaje_seleccionado: dict = random.choice(list(personajes.values()))
    juego_iniciado: bool = False
    juego_ganado: bool = False
    personajes_eliminados: dict[str, bool] = {clave: False for clave in personajes.keys()}

@pytest.fixture
def estado():
    return EstadoJuego()

def test_iniciar_juego(estado):
    assert estado.personaje_seleccionado is not None