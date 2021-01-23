from Boris import *
from Bat import *
from Granny import *
from Projectile import *
from Lifeform import *
import pygame
import os

FPS = 60
clock = pygame.time.Clock()

window_width, window_height = 750, 750
gameWindow = pygame.display.set_mode((window_width, window_height))
background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background.png")),
                                    (window_width, window_height))

############################# ASSETS #############################
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


###################################################################

def update(gameState):
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
    gameState = {
        "lost": False,
        "bats": [],
        "powerups": [],
        "healthUps": [],
        "bojo": Boris(300, 630),
        "gran": Granny()
    }

    while True:
        clock.tick(FPS)
        update(gameState)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                gameState["bojo"].shootVaccine()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            gameState["bojo"].shootVaccine()


#     TODO: Check collisions between bojo's vaccines and bats,
#     TODO: Ask the bats if they or their coronas have hit granny or bojo
#     TODO: Tell granny to move
#     TODO: Tell the bats to move
#     TODO: sync mouse with bojo
#     TODO: implement main menu with the back story and control info.
#     TODO: countdown timer; pre return to main menu.
#     TODO: Add audio elements when getting infected; or killing a bat.



if __name__ == '__main__':
    main()
