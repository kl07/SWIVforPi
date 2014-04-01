'''
Created on Apr 1, 2014

@author: Kevin
'''
from gameUnits import GameObject 
import pygame

class BasicBullet(GameObject.GameObject):

    def __init__(self, initX, initY):
        super(BasicBullet, self).__init__("basic bullet", [0, 6], pygame.image.load("images/bu1.gif").convert())
        self.rect = GameObject.GameObject.getRect(self)
        self.rect.x = initX
        self.rect.y = initY
        self.sfx = pygame.mixer.Sound("blast.wav")
        
    def update(self):
        if(self.rect.y > 0):
            self.rect = self.rect.move([0,-GameObject.GameObject.getSpeed(self)[1]])
        else:
            self.alive = 0