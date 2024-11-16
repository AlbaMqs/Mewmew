import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))  # Exemple : fond noir

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
