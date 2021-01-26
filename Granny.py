from Lifeform import *

"""
        Usage!

        1. instantiate granny
        2. call walk to make her walk, she figures it out on her own.
        3. call draw to bring her into existance.
"""


class Granny(Lifeform):

    def __init__(self, window_width=750, window_height=750):

        self.right_walk = [
            pygame.image.load(os.path.join("Assets/granny", f"{x + 1}.png")) for x in range(7)
        ]

        self.left_walk = [pygame.transform.flip(x, True, False) for x in self.right_walk]

        self.animation = self.right_walk
        self.frame = 0
        self.animationCounter = 0

        self.window_width = window_width
        self.direction = "right"
        self.vel = 1

        super().__init__(100, window_height - self.left_walk[0].get_height() - 20, self.right_walk[0], 1)

    def walk(self):

        self.move(2, self.vel)  # Super function call to move in the desired direction.

        if self.x > self.window_width - self.icon.get_width():  # Hits the left wall
            self.direction = "left"  # to query our dictionary of granny assets later.
            self.vel = self.vel * (-1)  # to switch the direction she walks
            # self.icon = self.img[self.direction]     # update the granny icon, to reflect change of direction.
            self.animation = self.left_walk

        elif self.x < self.icon.get_width() and self.direction == "left":  # Hits the right wall
            self.direction = "right"
            self.vel = self.vel * (-1)
            # self.icon = self.img[self.direction]
            self.animation = self.right_walk


    def draw(self, gamewindow):
        if self.animationCounter == 0:
            self.frame = (self.frame + 1) % 7
            self.animationCounter += 7
        else:
            self.animationCounter -= 1

        self.icon = self.animation[self.frame]
        super().draw(gamewindow)  # Draw the granny
        self.status_bar(gamewindow)  # Draw her health
