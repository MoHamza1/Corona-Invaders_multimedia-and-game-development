from Lifeform import *
from Projectile import *

"""
        Usage!
        
        1. pass the array of OS loaded pygame image objects,
        
        2. decide which virus, and git it in the same format as 1
        
        
        3.  Dead Checklist:
        
            Update the animation array when dead,
            set the frame and frame counter to 0;
            Alive state will be set to dead when boris detects one of his vaccines has collided.
            only pop it from the array once the animation frame == 4 && alive == False
            
        4. Check for collisions; call Bat_or_virus_collison on granny and boris, returns true if there is.
"""

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
        self.vel = 1 # positive because it is pointing downwards.

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
        # To prevent bat from shooting multiple virusses at a time.
        # THIS MAY BE REDUNDANT!!
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
        super().move(1, self.vel) # direction = 1 because it is pointing downwards.

        # And move all the virusses shot too
        for virus in self.shotViruses:
            virus.move()
            if virus.despawn():
                self.shotViruses.remove(virus)
        self.lock_and_load()
