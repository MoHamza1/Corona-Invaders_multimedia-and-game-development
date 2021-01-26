from Boris import *
from Bat import *
from Granny import *
from Projectile import *
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
        if powerup.despawn():
            gameState['powerups'].remove(powerup)

    for healthUp in gameState['healthUps']:
        healthUp.draw(gameWindow)
        if healthUp.despawn():
            gameState['healthUps'].remove(healthUp)

    for bat in gameState['bats']:
        if random.randrange(0, 15) == 1 and bat.y > 0:
            bat.infect()
        bat.draw(gameWindow)
        if bat.despawn() or (not bat.alive and bat.frame == 4):
            gameState['bats'].remove(bat)

    gameState['bojo'].draw(gameWindow)
    gameState['gran'].draw(gameWindow)

    if gameState['lost']:
        # lost_label = lost_font.render(f"You killed {gameState['kills']} bats!", 1, (255, 255, 255))
        # gameWindow.blit(lost_label, (window_width / 2 - lost_label.get_width() / 2, 350))

        high_score = lost_font.render(f"You killed {gameState['kills']} bats!", 1, (255, 255, 255))
        gameWindow.blit(high_score, (window_width / 2 - high_score.get_width() / 2, 350))
        game_over = lost_font.render(f"Game Over!", 1, (255, 255, 255))
        gameWindow.blit(game_over, (window_width / 2 - game_over.get_width() / 2, 320 - high_score.get_height()))

    pygame.display.update()


def main(difficulty):
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
        "kills": 0
    }
    post_game_timer = 0

    while True:
        clock.tick(FPS)

        # Check game controls

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        update(gameState)

        if not gameState["lost"]:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                gameState["bojo"].shootVaccine()

            # update the game screen

            # decide to spawn some bats, lives, and powerups.

            if random.randrange(0, 2000) == 1 or (len(gameState["healthUps"]) == 0 and gameState["bojo"].health <= 50):
                gameState["healthUps"].append(
                    Projectile(random.randrange(50, window_width - 100), random.randrange(-200, -100), life, 1))

            if random.randrange(0, 2000) == 1 or (
                    len(gameState["powerups"]) == 0 and gameState["bojo"].vaccine_count <= 50):
                gameState["powerups"].append(
                    Projectile(random.randrange(50, window_width - 100), random.randrange(-200, -100), crate, 1))
            if not len(gameState["bats"]):
                gameState['level'] += 1
                temp = [Bat(random.randrange(50, window_width - 100), random.randrange(-1500, -100),
                            viruses[random.randrange(0, 3)]) for i in range(gameState['level'] *2       * difficulty)]
                gameState["bats"].extend(temp)

            # check for collisions

            for bat in gameState["bats"]:
                status = bat.Bat_or_virus_collison(gameState["bojo"])
                if status and bat.alive:
                    gameState["bojo"].health -= 10
                    if status == 2:
                        gameState["kills"] += 1
                        bat.die()
                status = bat.Bat_or_virus_collison(gameState["gran"])
                if status and bat.alive:
                    gameState["gran"].health -= 10
                    if status == 2:
                        bat.die()

            for healthup in gameState["healthUps"]:
                if healthup.collided(gameState["bojo"]):
                    gameState["bojo"].health = min(100, gameState["bojo"].health + 25)
                    gameState["healthUps"].remove(healthup)
                if healthup.collided(gameState["gran"]):
                    gameState["gran"].health = 100
                    gameState["healthUps"].remove(healthup)

            for powerup in gameState["powerups"]:
                if powerup.collided(gameState["bojo"]):
                    gameState["bojo"].vaccine_count += 50
                    gameState["powerups"].remove(powerup)

            gameState["bats"] = gameState["bojo"].vaccinated(gameState["bats"])

            # sync movement with mouse.
            pos = pygame.mouse.get_pos()
            gameState["bojo"].x = min(pos[0], window_width - 60)
            gameState["bojo"].y = max(pos[1], window_height // 2)

            # Move everything

            gameState['bojo'].move_vaccines()
            gameState['gran'].walk()
            for bat in gameState['bats']:
                bat.move()
            for powerup in gameState['powerups']:
                powerup.move()
            for healthUp in gameState['healthUps']:
                healthUp.move()

        if gameState["bojo"].health <= 0:
            if gameState["lives"] > 0:
                gameState["lives"] -= 1
                gameState["bojo"].health = 100
            else:
                gameState["lost"] = True
                post_game_timer += 1
        if gameState["gran"].health <= 0:
            gameState["lost"] = True
            post_game_timer += 1

        if gameState["lost"]:
            if post_game_timer > FPS * 6:
                break
            else:
                continue

    pregame_menu()


def pregame_menu():
    big_font = pygame.font.SysFont("comicsans", 70)
    little_font = pygame.font.SysFont("comicsans", 35)
    Difficulty = 5
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                main(Difficulty + 1)
            if event.type == pygame.KEYUP:
                Difficulty = (Difficulty % 10) + 1

        gameWindow.blit(background, (0, 0))
        title_label = big_font.render("Press the mouse to begin...", 1, (255, 255, 255))
        difficulty_control = little_font.render("Press any key to control difficulty", 1,
                                                      (255, 255, 255))
        dificulty_label = little_font.render((f"Difficulty: {Difficulty}"), 1, (255, 255, 255))

        instructions_label = big_font.render("Instructions:.", 1, (255, 0, 255))
        control_label_1 = little_font.render(("1. Move Boris with your mouse, and shoot with Space Bar"), 1,
                                                   (255, 0, 0))
        control_label_2 = little_font.render(("2. Collect ammo and health by travelling to them"), 1, (255, 0, 0))
        control_label_3 = little_font.render(("3. Try to protect granny from the bats and their pesky virusses"), 1,
                                                   (255, 0, 0))

        cumDistance = 350
        gameWindow.blit(title_label, (window_width / 2 - title_label.get_width() / 2, cumDistance))
        cumDistance += title_label.get_height()
        gameWindow.blit(difficulty_control, (window_width / 2 - difficulty_control.get_width() / 2, cumDistance))
        cumDistance += difficulty_control.get_height() + 100


        gameWindow.blit(instructions_label, (window_width / 2 - instructions_label.get_width() / 2, cumDistance))
        cumDistance += instructions_label.get_height() + 20
        gameWindow.blit(control_label_1, (window_width / 2 - control_label_1.get_width() / 2, cumDistance))
        cumDistance += control_label_1.get_height()
        gameWindow.blit(control_label_2, (window_width / 2 - control_label_2.get_width() / 2, cumDistance))
        cumDistance += control_label_2.get_height()
        gameWindow.blit(control_label_3, (window_width / 2 - control_label_3.get_width() / 2, cumDistance))

        gameWindow.blit(dificulty_label, (15, 15))
        pygame.display.update()

    pygame.quit()


#     TODO: Add audio elements when getting infected; or killing a bat.


pregame_menu()
