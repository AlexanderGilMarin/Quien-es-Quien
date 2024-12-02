import pygame
import reflex

# Inicializamos Pygame
pygame.init()

# Configuración de la ventana
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tablero ¿Quién es quién?")

# Lista de personajes con sus nombres (sin las características por ahora)
personajes = [
    "Susan", "Claire", "David", "Anne", "Robert", "Anita", "Joe", "George", 
    "Bill", "Alfred", "Max", "Tom", "Alex", "Sam", "Richard", "Paul", "Maria", 
    "Frans", "Herman", "Bernard", "Philip", "Eric", "Charles", "Peter"
]

# Clase del juego
class Juego(reflex.Game):
    def __init__(self):
        super().__init__()
        self.personajes_restantes = personajes

    def dibujar_tablero(self):
        # Dibujar todos los personajes en el tablero
        font = pygame.font.SysFont("Arial", 24)
        x, y = 20, 50
        for personaje in self.personajes_restantes:
            text = font.render(personaje, True, (255, 255, 255))  # Texto en blanco
            screen.blit(text, (x, y))
            y += 40  # Espacio entre personajes

    def actualizar(self):
        # Limpiar la pantalla
        screen.fill((0, 0, 0))  # Fondo negro
        self.dibujar_tablero()  # Dibujar el tablero con los personajes
        pygame.display.update()  # Actualizar la pantalla

# Ejecutar el juego
if __name__ == "__main__":
    juego = Juego()
    juego.run()  # Inicia el ciclo del juego