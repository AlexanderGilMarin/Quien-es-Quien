import reflex as rx 
import random
from Quien_es_Quien.personaje_aleatorio import personajes


class GameState(rx.State):
    question: str = ""
    chat_history: list[tuple[str, str]] = []
    selected_character: dict = random.choice(list(personajes.values()))
    choices: dict[str, bool] = {
        k: False for k in personajes.keys()  
    }

    def check_choice(self, value, character):
        self.choices[character] = value

    @rx.event
    async def answer(self):
        question = self.question.lower().strip()
        self.question = ""  
        respuesta = "No entiendo la pregunta."

        
        if "es" in question and any(word in question for word in ["el personaje"]):
            if self.selected_character["nombre"].lower() in question:
                respuesta = f"¡Sí! El personaje es {self.selected_character['nombre']}."
            else:
                respuesta = "No, no es ese personaje."
        
       
        elif any(keyword in question for keyword in ["tiene", "lleva", "es"]):
            for caract in self.selected_character["características"]:
                if caract.lower() in question:
                    respuesta = "Sí"
                    break
            else:
                
                respuesta = "No"

        
        else:
            respuesta = "No entiendo tu pregunta. Intenta preguntar por características o nombres."

        
        self.chat_history.append((question, respuesta))

    @rx.event
    async def clear_chat(self):
        """Limpia el historial del chat."""
        self.chat_history.clear()


def qa(question: str, answer: str) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(question, style={"text-align": "right"}),
            bg="LightGray",
            padding="10px",
            border_radius="8px",
            margin_y="5px",
        ),
        rx.box(
            rx.text(answer, style={"text-align": "left"}),
            bg="LightGreen",
            padding="10px",
            border_radius="8px",
            margin_y="5px",
        ),
        spacing="2",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            GameState.chat_history,
            lambda msg: qa(msg[0], msg[1]),
        ),
        padding="20px",
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=GameState.question,
            placeholder="Haz una pregunta sobre el personaje",
            on_change=GameState.set_question,
            style={"width": "350px", "padding": "10px", "border-radius": "8px"},
        ),
        rx.button(
            "Preguntar",
            on_click=GameState.answer,
            style={"background-color": "LightBlue", "padding": "10px", "border-radius": "8px"},
        ),
        rx.button(
            "Limpiar Chat",  
            on_click=GameState.clear_chat,
            style={"background-color": "LightCoral", "padding": "10px", "border-radius": "8px"},
        ),
        spacing="3",
    )


def tablero() -> rx.Component:
    personajes_lista = list(personajes.values())

    filas = []
    for i in range(0, len(personajes_lista), 6):
        fila = rx.hstack(
            [
                rx.box(
                    rx.image(
                        src=personaje["imagen"],
                        alt=personaje["nombre"],
                        width="100px",
                        height="100px",
                    ),
                    rx.text(personaje["nombre"], font_size="14px"),
                    rx.checkbox(),  
                    bg="LightGray",
                    padding="10px",
                    border_radius="8px",
                    margin="5px",
                    text_align="center",
                )
                for personaje in personajes_lista[i:i + 6]
            ],
            spacing="3",
        )
        filas.append(fila)

    return rx.center(
        rx.vstack(*filas, spacing="3"),
        padding="20px",
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.text("Adivina quién es el personaje", font_size="24px", color="black"),
            tablero(),
            chat(),
            action_bar(),
            align="center",
        ),
        padding="20px",
    )


app = rx.App()
app.add_page(index, route="/", title="¿Quién es quién?")
app._compile()