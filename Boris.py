from Lifeform import *


class Boris(Lifeform):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, pygame.image.load(os.path.join("Assets", "boris.png")))

    def shootVaccine(self):
        pass
        # obv

    def draw(self, gamewindow):
        pass
        # Draw self and all my vaccines

    def vaccinate(self):
        pass
        # Detect collisons of vaccines with any bats

    def status_bar(self):
        pass
        # obvious
