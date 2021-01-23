import Boris
import Bat
import Granny
import Projectile
import pygame
import os


window_width, window_height = 750, 750
gameWindow = pygame.display.set_mode((window_width, window_height))
background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background.png")), (window_width, window_height))

flying_bat = [
    pygame.image.load(os.path.join("Assets/Flying_Bat", f"flying_bat_{x + 1}.png")) for x in range(5)
]
dead_bat = [
    pygame.image.load(os.path.join("Assets/Dead_Bat", f"DEAD_{x + 1}.png")) for x in range(5)
]

life = pygame.image.load(os.path.join("Assets", "life.png"))
crate = pygame.image.load(os.path.join("Assets", "crate.png"))

viruses = [
    pygame.image.load(os.path.join("Assets", f"virus_{x}.png")) for x in ['blue', 'green', 'red']
]



