from Lifeform import *
from Projectile import *

"""
        Usage!

        1. instantiate boris
        2. update x y locations by whatever method, mouse keyboard etc.
        3. call draw to bring him into existance.
        4. call shootVaccine to shoot
        5. call vaccinated on an array of bat objects to dect vaccine -> bat collisions. 
"""


class Boris(Lifeform):

    def __init__(self, x, y):
        super().__init__(x, y, pygame.image.load(os.path.join("Assets", "boris.png")))
        self.vaccinesShot = []
        self.vaccine_count = 100
        self.canShoot = 0

    def shootVaccine(self):
        # Create instance of Projectile with vaccine icon and vel -5 to point upwards.

        if not self.canShoot:
            self.vaccinesShot.append(
                Projectile(self.x, self.y, pygame.image.load(os.path.join("Assets", "vaccine.png")), -5))

    def draw(self, gamewindow):
        super().draw(gamewindow)
        self.recoil()  # call the count down function to enable shooting again.
        for vaccine in self.vaccinesShot:  # Draw all the vaccines.
            vaccine.draw()
        pass
        # Draw self and all my vaccines

    def move_vaccines(self):
        for vaccine in self.vaccinesShot:
            vaccine.move()

    def vaccinated(self, bats):
        temp = bats
        for vaccine in self.vaccinesShot:
            for bat in temp:
                if vaccine.collided(bat):
                    bat.alive = False
        return temp

    def status_bar(self):
        pass

    def recoil(self):
        # To prevent the user from accidentally shooting too many vaccines
        self.canShoot = 0 if self.canShoot > 30 else (self.canShoot + 1)
