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
        super().__init__(x, y, pygame.image.load("./Assets/boris.png"))
        self.vaccinesShot = []
        self.vaccine_count = 100
        self.canShoot = 0

    def shootVaccine(self):
        # Create instance of Projectile with vaccine icon and vel -5 to point upwards.

        if not self.canShoot and self.vaccine_count > 0:
            from pygame import mixer
            shoot_vaccine = mixer.Sound('./Assets/sounds/shoot.wav')
            shoot_vaccine.play()
            self.vaccine_count -=1
            self.vaccinesShot.append(
                Projectile(self.x, self.y, pygame.image.load("./Assets/vaccine.png"), -5))

    def draw(self, gamewindow):
        super().draw(gamewindow)
        self.recoil()  # call the count down function to enable shooting again.
        self.status_bar(gamewindow)
        for vaccine in self.vaccinesShot:  # Draw all the vaccines that are in range, otherwise remove them.
            if vaccine.y > 0:
                vaccine.draw(gamewindow)
            else:
                self.vaccinesShot.remove(vaccine)
        pass
        # Draw self and all my vaccines

    def move_vaccines(self):
        for vaccine in self.vaccinesShot:
            vaccine.move()
            if vaccine.despawn():
                self.vaccinesShot.remove(vaccine)


    def vaccinated(self, bats):
        temp = bats
        for vaccine in self.vaccinesShot:
            for bat in temp:
                if vaccine.collided(bat) and bat.alive:
                    try:
                        self.vaccinesShot.remove(vaccine)
                        bat.die()
                    except:
                        pass
        return temp


    def recoil(self):
        # To prevent the user from accidentally shooting too many vaccines
        self.canShoot = 0 if self.canShoot > 15 else (self.canShoot + 2)
