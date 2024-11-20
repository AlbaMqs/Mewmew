import pygame
from src.character import Character
from settings import BASE_SPEED, START_SPEED, SPEED_INTERPOLATION_FACTOR

class Player:
    def __init__(self, name, x, y):
        """
        Crée un joueur avec un personnage attaché.
        :param name: Nom du personnage
        :param x: Position initiale x
        :param y: Position initiale y
        """
        self.character = Character(name, x, y)
        self.base_speed = BASE_SPEED  # Vitesse de base
        self.speed = self.base_speed  # Vitesse cible (normale ou sprint)
        self.current_speed = self.base_speed * START_SPEED  # Vitesse interpolée

        # Initialiser la manette
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

    def get_input_vector(self):
        """
        Calcule le vecteur de déplacement en fonction des entrées clavier ou manette.
        :return: Tuple (move_x, move_y) représentant le vecteur directionnel.
        """
        move_x, move_y = 0, 0

        # Priorité au stick gauche de la manette
        if self.joystick:
            deadzone = 0.2  # Zone morte pour ignorer les petits mouvements du stick
            axis_x = self.joystick.get_axis(0)  # Axe horizontal du stick gauche
            axis_y = self.joystick.get_axis(1)  # Axe vertical du stick gauche

            # Ignorer les mouvements trop petits (zone morte)
            if abs(axis_x) > deadzone:
                move_x = axis_x
            if abs(axis_y) > deadzone:
                move_y = axis_y

        # Si aucun mouvement de la manette, lire le clavier
        if move_x == 0 and move_y == 0:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_z]:  # Haut
                move_y = -1
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:  # Bas
                move_y = 1

            if keys[pygame.K_LEFT] or keys[pygame.K_q]:  # Gauche
                move_x = -1
            elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Droite
                move_x = 1

        return move_x, move_y

    def handle_speed(self):
        """
        Gère la vitesse cible en fonction des entrées.
        Si Shift ou le bouton X de la manette est enfoncé, double la vitesse.
        """
        keys = pygame.key.get_pressed()

        # Vérifie si Shift est appuyé
        is_shift_pressed = keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]

        # Vérifie si le bouton X de la manette est pressé (souvent le bouton 0)
        is_x_button_pressed = False
        if self.joystick:
            is_x_button_pressed = self.joystick.get_button(0)

        # Ajuste la vitesse cible
        if is_shift_pressed or is_x_button_pressed:
            self.speed = self.base_speed * 2
        else:
            self.speed = self.base_speed

    def interpolate_speed(self, dt):
        """
        Interpole la vitesse actuelle vers la vitesse cible.
        :param dt: Temps écoulé depuis la dernière frame (en millisecondes)
        """
        interpolation_amount = SPEED_INTERPOLATION_FACTOR * (dt / 1000)
        if self.current_speed < self.speed:
            self.current_speed = min(self.current_speed + interpolation_amount, self.speed)
        elif self.current_speed > self.speed:
            self.current_speed = max(self.current_speed - interpolation_amount, self.speed)

    def handle_movement(self, dt, move_x, move_y):
        """
        Gère le déplacement du personnage en fonction d'un vecteur de direction.
        :param dt: Temps écoulé depuis la dernière frame (en millisecondes)
        :param move_x: Composante X du vecteur directionnel
        :param move_y: Composante Y du vecteur directionnel
        """
        # Interpolation de la vitesse
        self.interpolate_speed(dt)

        # Normalisation du vecteur de déplacement
        length = (move_x**2 + move_y**2)**0.5
        if length != 0:  # Éviter la division par zéro
            move_x = (move_x / length) * self.current_speed * (dt / 1000)
            move_y = (move_y / length) * self.current_speed * (dt / 1000)

        # Si aucun mouvement n'est détecté, passer à l'état idle
        if move_x == 0 and move_y == 0:
            self.character.stop()
        else:
            # Déplacer le personnage
            new_x = self.character.x + move_x
            new_y = self.character.y + move_y
            self.character.move(new_x, new_y)

    def handle_input(self, dt):
        """
        Gère les commandes clavier et manette pour déplacer le personnage.
        :param dt: Temps écoulé depuis la dernière frame (en millisecondes)
        """
        self.handle_speed()  # Ajuste la vitesse cible en fonction des entrées
        move_x, move_y = self.get_input_vector()
        self.handle_movement(dt, move_x, move_y)

    def update(self, dt):
        self.character.update(dt)

    def draw(self, screen):
        self.character.draw(screen)
