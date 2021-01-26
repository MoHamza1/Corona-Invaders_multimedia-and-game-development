import pygame
import os

class Lifeform:

    def __init__(self,x,y,icon,window_height=750):
        self.x = x
        self.y = y
        self.health = 100
        self.mask = pygame.mask.from_surface(icon)  # For pygame's native collision detection
        self.icon = icon                            # Projectiles are assosiated with different assets.
        self.window_height = window_height          # To check if we need to despawn later.

    def draw(self, gamewindow):
        # Draw method for the projectile.
        gamewindow.blit(self.icon, (self.x, self.y))

    def move(self,direction,vel):
        # Direction 1: upwards/downwards
        # Direction 2: right/left
        self.y += vel if direction == 1 else 0
        self.x += vel if direction == 2 else 0

    def is_off_screen(self):
            return True if 0 <= self.y <= self.window_height else False

    def status_bar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.icon.get_height() + 10, self.icon.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.icon.get_height() + 10, self.icon.get_width() * (self.health/100), 10))




