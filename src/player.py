import pygame
from src.character import Character
from settings import BASE_SPEED

class Player:
    def __init__(self, name, x, y):
        """
        Crée un joueur avec un personnage attaché.
        :param name: Nom du personnage
        :param x: Position initiale x
        :param y: Position initiale y
        """
        self.character = Character(name, x, y)
        self.speed = BASE_SPEED  # Vitesse du joueur en pixels par seconde

        # Initialiser la manette
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(f"Manette connectée : {self.joystick.get_name()}")

    def handle_input(self, dt):
        """
        Gère les commandes clavier pour déplacer le personnage.
        :param dt: Temps écoulé depuis la dernière frame (en millisecondes)
        """
        keys = pygame.key.get_pressed()
        move_x, move_y = 0, 0

        # Flèches directionnelles ou ZQSD
        if keys[pygame.K_UP] or keys[pygame.K_z]:  # Haut (flèche haut ou Z)
            move_y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:  # Bas (flèche bas ou S)
            move_y = 1

        if keys[pygame.K_LEFT] or keys[pygame.K_q]:  # Gauche (flèche gauche ou Q)
            move_x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Droite (flèche droite ou D)
            move_x = 1

        # Normalisation du vecteur de déplacement
        length = (move_x**2 + move_y**2)**0.5
        if length != 0:  # Éviter la division par zéro
            move_x = (move_x / length) * self.speed * (dt / 1000)
            move_y = (move_y / length) * self.speed * (dt / 1000)

        # Si aucun mouvement n'est détecté, passer à l'état idle
        if move_x == 0 and move_y == 0:
            self.character.stop()
        else:
            # Déplacer le personnage
            new_x = self.character.x + move_x
            new_y = self.character.y + move_y
            self.character.move(new_x, new_y)

    def update(self, dt):
        """
        Met à jour le personnage.
        :param dt: Temps écoulé depuis la dernière frame (en millisecondes)
        """
        self.character.update(dt)

    def draw(self, screen):
        """
        Dessine le personnage à l'écran.
        :param screen: Surface de l'écran
        """
        self.character.draw(screen)
