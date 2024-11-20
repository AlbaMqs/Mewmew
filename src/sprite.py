#sprite.py
import pygame
from settings import ZOOM_CAM, FRAMERATE
import os

class AnimatedSprite:
    def __init__(self, prefix, folder_path, max_frames):
        """
        :param prefix: Préfixe des fichiers d'animation (ex: "base_idle_")
        :param folder_path: Dossier contenant les images
        :param max_frames: Nombre maximum d'images dans l'animation
        :param zoom: Facteur de redimensionnement
        :param frame_rate: Images par seconde pour l'animation
        """
        self.images = []
        self.current_frame = 0
        self.frame_rate = FRAMERATE
        self.time_since_last_frame = 0  # Pour le contrôle du timing

        # Charger toutes les images jusqu'à max_frames
        for i in range(max_frames):
            file_name = f"{prefix}{i:03}.png"  # Format : base_idle_000.png
            file_path = os.path.join(folder_path, file_name)
            if os.path.exists(file_path):  # Vérifie si l'image existe
                image = pygame.image.load(file_path).convert_alpha()
                if ZOOM_CAM != 1.0:
                    image = pygame.transform.scale(
                        image, 
                        (int(image.get_width() * ZOOM_CAM), int(image.get_height() * ZOOM_CAM))
                    )
                self.images.append(image)
            else:
                raise ValueError(f"L'image {file_name} est introuvable dans le dossier {folder_path}.")

        if not self.images:
            raise ValueError(f"Aucune image trouvée avec le préfixe '{prefix}' dans le dossier '{folder_path}'.")

        # Rectangle pour positionner le sprite
        self.rect = self.images[0].get_rect()

    def update(self, dt):
        """
        Met à jour l'image courante en fonction du temps écoulé.
        :param dt: Temps écoulé depuis la dernière mise à jour (en millisecondes)
        """
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= 1000 / self.frame_rate:
            self.time_since_last_frame = 0
            self.current_frame = (self.current_frame + 1) % len(self.images)

    def draw(self, screen, x, y):
        """
        Affiche l'image courante à la position spécifiée.
        :param screen: Surface de l'écran
        :param x: Position x
        :param y: Position y
        """
        self.rect.topleft = (x, y)
        screen.blit(self.images[self.current_frame], self.rect)
