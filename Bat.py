from Lifeform import *
from Projectile import *


class Bat(Lifeform):

    def __init__(self, x, y, bat_animation, virusStrain):

        self.animation = bat_animation
        self.frame = 0
        self.animationCounter = 0
        self.virusStrain = virusStrain
        super().__init__(x, y, self.animation[self.frame], 1)
        self.shotViruses = []
        self.alive = True
        self.locked_and_loaded = 0
        self.vel = 1

    def draw(self, gamewindow):
        if self.animationCounter == 0:
            self.frame = (self.frame + 1) % 5
            self.animationCounter += 5
        else:
            self.animationCounter -= 1

        super().icon = self.animation[self.frame]
        super().draw(gamewindow)

        for virus in self.shotViruses:
            virus.draw(gamewindow)

    def infect(self):
        if self.alive and not self.locked_and_loaded:
            self.shotViruses.append(Projectile(self.x, self.y, self.virusStrain, 5))
            self.locked_and_loaded = not self.locked_and_loaded

    def lock_and_load(self):
        self.locked_and_loaded = 0 if self.locked_and_loaded > 30 else (self.locked_and_loaded + 1)

    def Bat_or_virus_collison(self, target):
        # we check if any of our viruses hit a target;
        for virus in self.shotViruses:
            if virus.collided(target):
                return True
        # we check this bat hit a target in case none of the virusses did.
        return True if self.mask.overlap(target.mask, ((target.x - self.x), (target.y - self.y))) else False

    def move(self):
        # We move the bat first
        super().move(1, self.vel)

        # And move all the virusses shot too
        for virus in self.shotViruses:
            virus.move()
            if virus.despawn():
                self.shotViruses.remove(virus)
