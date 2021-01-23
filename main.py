import Boris
import Bat
import Granny
import Projectile
import Lifeform
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
vaccine = pygame.image.load(os.path.join("Assets", "vaccine.png"))

viruses = [
    pygame.image.load(os.path.join("Assets", f"virus_{x}.png")) for x in ['blue', 'green', 'red']
]

main_font = pygame.font.SysFont("comicsans", 50)
lost_font = pygame.font.SysFont("comicsans", 60)

def redraw_window(gameState):

    gameWindow.blit(background, (0, 0))
    lives_label = main_font.render(f"{gameState['lives']}", 1, (255, 255, 255))
    vaccine_label = main_font.render(f"{gameState['vaccine_count']}", 1, (255, 255, 255))
    level_label = main_font.render(f"Level: {gameState['level']}", 1, (255, 255, 255))

    gameWindow.blit(life, (10, 10))
    gameWindow.blit(lives_label, (life.get_width() + 25, 15))
    gameWindow.blit(vaccine, (window_width / 2 - 50, 10))
    gameWindow.blit(vaccine_label, (window_width / 2 + vaccine.get_width() - 25, 15))
    gameWindow.blit(level_label, (window_width - level_label.get_width() - 10, 10))

    for powerup in gameState['powerups']:
        powerup.draw(gameWindow)

    for healthUp in gameState['healthUps']:
        healthUp.draw(gameWindow)

    for enemy in gameState['enemies']:
        enemy.draw(gameWindow)

    gameState['player'].draw(gameWindow)

    if gameState['lost']:
        lost_label = lost_font.render("You Lost!!", 1, (255, 255, 255))
        gameWindow.blit(lost_label, (window_width / 2 - lost_label.get_width() / 2, 350))

    pygame.display.update()



def main():
    print("hello wrld")

if __name__ == '__main__':
    main()


