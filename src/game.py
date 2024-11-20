import pygame
from src.player import Player

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

        # Créer un joueur
        self.player = Player(name="base", x=100, y=100)

    def update(self, dt):
        # Gérer les entrées utilisateur et mettre à jour le joueur
        self.player.handle_input(dt)
        self.player.update(dt)

    def draw(self):
        # Dessiner le joueur
        self.screen.fill((0, 0, 0))  # Fond noir
        self.player.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
