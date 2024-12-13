import reflex as rx
import random
from Quien_es_Quien.personaje_aleatorio import personajes


class EstadoJuego(rx.State):
    pregunta: str = ""
    historial_chat: list[tuple[str, str]] = []
    personaje_seleccionado: dict = random.choice(list(personajes.values()))
    juego_iniciado: bool = False
    juego_ganado: bool = False
    personajes_eliminados: dict[str, bool] = {k: False for k in personajes.keys()}

    @rx.event
    async def responder(self):
        pregunta = self.pregunta.lower().strip()
        self.pregunta = ""
        respuesta = "No entiendo la pregunta."

        if "es" in pregunta and "el personaje" in pregunta:
            nombre_personaje = self.personaje_seleccionado["nombre"].lower()
            if nombre_personaje in pregunta:
                respuesta = f"¡Sí! El personaje es {self.personaje_seleccionado['nombre']}."
                self.juego_ganado = True
            else:
                respuesta = "No, no es ese personaje."
                self._eliminar_personaje(pregunta)

        elif any(palabra_clave in pregunta for palabra_clave in ["tiene", "lleva", "es"]):
            respuesta = self._manejar_pregunta_caracteristica(pregunta)

        self.historial_chat.append((pregunta, respuesta))

    def _eliminar_personaje(self, pregunta):
        nombre_personaje = pregunta("el personaje")[-1]
        if nombre_personaje in self.personajes_eliminados:
            self.personajes_eliminados[nombre_personaje] = True

    def _manejar_pregunta_caracteristica(self, pregunta):
        respuesta = "No"
        tiene_caracteristica = False
        for caracteristica in self.personaje_seleccionado["características"]:
            if caracteristica in pregunta:
                tiene_caracteristica = True
                respuesta = "Sí"
                self._eliminar_personajes_sin_caracteristica(pregunta)
                break
        if not tiene_caracteristica:
            self._eliminar_personajes_con_caracteristica(pregunta)
        return respuesta

    def _eliminar_personajes_sin_caracteristica(self, pregunta):
        for nombre, personaje in personajes.items():
            if not any(c in pregunta for c in personaje["características"]):
                self.personajes_eliminados[nombre] = True

    def _eliminar_personajes_con_caracteristica(self, pregunta):
        for nombre, personaje in personajes.items():
            if any(c in pregunta for c in personaje["características"]):
                self.personajes_eliminados[nombre] = True

    @rx.event
    async def iniciar_juego(self):
        self.juego_iniciado = True
        self.personaje_seleccionado = random.choice(list(personajes.values()))
        self.historial_chat.clear()
        self.personajes_eliminados = {k: False for k in personajes.keys()}

    @rx.event
    async def nuevo_juego(self):
        self.juego_iniciado = False
        self.juego_ganado = False
        self.historial_chat.clear()
        self.pregunta = ""
        self.personajes_eliminados = {k: False for k in personajes.keys()}

    @rx.event
    async def limpiar_chat(self):
        self.historial_chat.clear()

    @rx.event
    async def establecer_pregunta(self, valor: str):
        self.pregunta = valor


def pantalla_inicio() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("¿Quién es Quién?", font_size="2em"),
            rx.button("Comenzar Juego", on_click=EstadoJuego.iniciar_juego, style={"background-color": "LightBlue", "padding": "20px", "border-radius": "8px", "font-size": "1.2em"}),
            spacing="8", padding="100px",
        )
    )


def pr(pregunta: str, respuesta: str) -> rx.Component:
    return rx.vstack(
        rx.box(rx.text(pregunta, style={"text-align": "right"}), bg="LightCoral", padding="10px", border_radius="8px", margin_y="5px"),
        rx.box(rx.text(respuesta, style={"text-align": "left"}), bg="LightBlue", padding="10px", border_radius="8px", margin_y="5px"),
        spacing="2",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(EstadoJuego.historial_chat, lambda msg: pr(msg[0], msg[1])),
        padding="20px", color="black"
    )


def barra_acciones() -> rx.Component:
    return rx.hstack(
        rx.input(value=EstadoJuego.pregunta, placeholder="Haz una pregunta sobre el personaje", on_change=EstadoJuego.establecer_pregunta, style={"width": "350px", "padding": "10px", "border-radius": "8px"}),
        rx.button("Preguntar", on_click=EstadoJuego.responder, style={"background-color": "LightBlue", "padding": "10px", "border-radius": "8px", "color":"black"}),
        rx.button("Limpiar Chat", on_click=EstadoJuego.limpiar_chat, style={"background-color": "LightCoral", "padding": "10px", "border-radius": "8px", "color":"black"}),
        rx.button("Nuevo Juego", on_click=EstadoJuego.nuevo_juego, style={"background-color": "LightGreen", "padding": "10px", "border-radius": "8px", "color":"black"}),
        spacing="3",
    )


def tablero() -> rx.Component:
    lista_personajes = list(personajes.values())
    filas = [
        rx.hstack(
            [
                rx.box(
                    rx.image(src=personaje["imagen"], alt=personaje["nombre"], width="100px", height="100px"),
                    rx.text(personaje["nombre"], font_size="16px", color="black"),
                    bg="LightBlue", padding="10px", border_radius="8px", margin="5px", text_align="center",
                    opacity=rx.cond(EstadoJuego.personajes_eliminados[personaje["nombre"]], "0", "1"),
                )
                for personaje in lista_personajes[i:i + 6]
            ], spacing="3",
        )
        for i in range(0, len(lista_personajes), 6)
    ]
    return rx.center(rx.vstack(*filas, spacing="3"), padding="20px")


def index() -> rx.Component:
    return rx.cond(
        EstadoJuego.juego_iniciado,
        rx.center(
            rx.vstack(
                rx.cond(EstadoJuego.juego_ganado, rx.heading("¡Felicidades! ¡Has ganado!", color="green", font_size="2em"), rx.text("Adivina quién es el personaje", font_size="24px", color="LightBlue")),
                rx.hstack(
                    rx.box(tablero(), width="70%"),
                    rx.box(chat(), barra_acciones(), width="30%"),
                    width="100%", spacing="4",
                ),
                align="center",
            ),
            padding="20px",
        ),
        pantalla_inicio(),
    )


app = rx.App()
app.add_page(index, route="/", title="¿Quién es quién?")
app._compile()