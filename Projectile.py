import pygame


class Projectile:
    def __init__(self, x, y, icon,speed, window_height=750):
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(icon)  # For pygame's native collision detection
        self.icon = icon                            # Projectiles are assosiated with different assets.
        self.window_height = window_height          # To check if we need to despawn later.
        self.speed = speed

    def draw(self, gamewindow):
        # Draw method for the projectile.
        gamewindow.blit(self.icon, (self.x, self.y))

    def move(self):
        # IF projectile is pointing upwards then speed < 0
        # otherwise speed is negative.

        self.y += self.speed

    def despawn(self):
        # We check to see if the projectile within the bounds of the screen,
        # Projectiles either point upwards or downwards.
        return True if self.window_height <= self.y >= 0 else False

    def collided(self, target):
        # We check if the projectile has hit its target by checking to see if the target's mask over laps with
        # the projectile's mask; pygame's native collison detection.
        # This is especially useful since if its assosiated with the physical colision the user can see.
        return True if self.mask.overlap(target.mask, ((target.x - self.x), (target.y - self.y))) else False
