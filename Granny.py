from Lifeform import *

"""
        Usage!

        1. instantiate granny
        2. call walk to make her walk, she figures it out on her own.
        3. call draw to bring her into existance.
"""

class Granny(Lifeform):

    def __init__(self, window_width=750, window_height=750):
        self.window_width = window_width
        self.direction = "right"
        self.vel = 1
        self.img = {
            "right": pygame.image.load(os.path.join("Assets", f"granny_right.png")),
            "left": pygame.image.load(os.path.join("Assets", f"granny_left.png"))
        }

        super().__init__(10, window_height - 50, self.img[self.direction],1 )

    def walk(self):

        self.move(2, self.vel)               # Super function call to move in the desired direction.

        if self.x > self.window_width - super().icon.get_width():   # Hits the left wall
            self.direction = "left"                     # to query our dictionary of granny assets later.
            self.vel = self.vel * (-1)                  # to switch the direction she walks
            super().icon = self.img[self.direction]     # update the granny icon, to reflect change of direction.
        elif self.x < super().icon.get_width():         # Hits the right wall
            self.direction = "right"
            self.vel = self.vel * (-1)
            super().icon = self.img[self.direction]

    def status_bar(self,gamewindow):
        pass
        # obvious

    def draw(self, gamewindow):
        super().draw(gamewindow)        # Draw the granny
        self.status_bar(gamewindow)     # Draw her health
