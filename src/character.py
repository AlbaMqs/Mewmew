import pygame
from src.sprite import AnimatedSprite

class Character:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

        self.state = "idle"
        self.direction = "down"

        self.sprite_folder = f"assets/sprites/characters/{self.name}/"
        self.max_frames = 8

        self.update_sprite()

    def update_sprite(self):
        """
        Met à jour l'animation en fonction de l'état et de la direction.
        """
        sprite_prefix = f"{self.name}_{self.state}_{self.direction}_"
        self.sprite = AnimatedSprite(sprite_prefix, self.sprite_folder, self.max_frames)

    def get_direction(self, new_x, new_y):
        """
        Calcule la direction en fonction de la différence entre les positions actuelles et nouvelles.
        """
        dx = new_x - self.x
        dy = new_y - self.y

        if abs(dy) > abs(dx):  # Mouvement vertical prioritaire
            direction = "down" if dy > 0 else "up"
        else:  # Mouvement horizontal prioritaire
            direction = "right" if dx > 0 else "left"
            
        return direction

    def move(self, new_x, new_y):
        new_direction = self.get_direction(new_x, new_y)

        if self.direction != new_direction:
            self.direction = new_direction
            self.update_sprite()

        if self.state != "run":
            self.state = "run"
            self.update_sprite()

        self.x = new_x
        self.y = new_y

    def stop(self):
        if self.state != "idle":
            self.state = "idle"
            self.update_sprite()

    def update(self, dt):
        """Met à jour le sprite du personnage (animation)."""
        self.sprite.update(dt)

    def draw(self, screen):
        """Affiche le sprite à l'écran."""
        self.sprite.draw(screen, self.x, self.y)
