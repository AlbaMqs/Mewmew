#game.py
import pygame
from src.sprite import AnimatedSprite

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        
        self.animated_sprite = AnimatedSprite(
            prefix="base_idle_down_", 
            folder_path="assets/sprites/characters/base/", 
            max_frames=7
        )

    def update(self, dt):
        self.animated_sprite.update(dt)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Exemple : fond noir
        self.animated_sprite.draw(self.screen, 100, 100)  # Dessiner le sprite

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
