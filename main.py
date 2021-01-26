from Boris import *
from Bat import *
from Granny import *
from Projectile import *
from Lifeform import *
import pygame
import os
import random

FPS = 60
clock = pygame.time.Clock()
pygame.font.init()
window_width, window_height = 750, 750
gameWindow = pygame.display.set_mode((window_width, window_height))
background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background.png")),
                                    (window_width, window_height))
pygame.mouse.set_visible(False)

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
    vaccine_label = main_font.render(f"{gameState['bojo'].vaccine_count}", 1, (255, 255, 255))
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

    for bat in gameState['bats']:
        bat.draw(gameWindow)
        if bat.despawn() or (not bat.alive and bat.frame == 4):
            gameState['bats'].remove(bat)

    gameState['bojo'].draw(gameWindow)
    gameState['gran'].draw(gameWindow)
    gameState['gran'].walk()

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
        "gran": Granny(),
        "lives": 5,
        "vaccine_count": None,
        "level": 1,
    }

    while True:
        clock.tick(FPS)

        # Check game controls

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                gameState["bojo"].shootVaccine()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            gameState["bojo"].shootVaccine()


        # update the game screen
        update(gameState)

        # decide to spawn some bats, lives, and powerups.

        if not len(gameState["bats"]):
            gameState['level'] += 1
            temp = [Bat(random.randrange(50, window_width-100), random.randrange(-1500, -100),flying_bat,viruses[random.randrange(0,3)]) for i in range(gameState['level'] * 5)]
            gameState["bats"].extend(temp)

        # check for collisions

        for bat in gameState["bats"]:
            if bat.Bat_or_virus_collison(gameState["bojo"]) and bat.alive:
                gameState["bojo"].health -= 10
                bat.die()
            if bat.Bat_or_virus_collison(gameState["gran"]) and bat.alive:
                gameState["gran"].health -= 10
                bat.die()

        gameState["bats"] = gameState["bojo"].vaccinated(gameState["bats"])



        # sync movement with mouse.
        pos = pygame.mouse.get_pos()
        gameState["bojo"].x = min(pos[0],window_width - 60)
        gameState["bojo"].y = max(pos[1],window_height//2)

        # Move everything
        gameState['bojo'].move_vaccines()
        for bat in gameState['bats']:
            bat.move()

#     TODO: implement main menu with the back story and control info.
#     TODO: countdown timer; pre return to main menu.
#     TODO: Add audio elements when getting infected; or killing a bat.



if __name__ == '__main__':
    main()
