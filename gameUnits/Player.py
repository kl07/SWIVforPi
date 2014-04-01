'''
Created on Mar 14, 2014

@author: Kevin
'''
import pygame
from gameUnits import GameObject

class Player(GameObject.GameObject):
      
    def __init__(self):
        super(Player, self).__init__("helicopter", [4, 4], pygame.image.load("images/p1.gif").convert())
        
        self.playerrect = GameObject.GameObject.getRect(self)
        
        self.animationIndex = 0
        self.copterBlades = []
        self.copterBlades.append(pygame.image.load("images/b1.gif"))
        self.copterBlades.append(pygame.image.load("images/b2.gif"))
        self.copterBlades.append(pygame.image.load("images/b3.gif"))        
        self.copterBlade = self.copterBlades[self.animationIndex]
    
    def update(self, keys):        
        self.updateCopterBlades()
        
        if keys[pygame.K_a] and (self.playerrect.x > 0):
            self.playerrect = self.playerrect.move([-GameObject.GameObject.getSpeed(self)[0], 0])
        if keys[pygame.K_d] and (self.playerrect.x < 200-self.playerrect.width): # Use static vars
            self.playerrect = self.playerrect.move([GameObject.GameObject.getSpeed(self)[0], 0])
        if keys[pygame.K_w] and (self.playerrect.y > 0):
            self.playerrect = self.playerrect.move([0,-GameObject.GameObject.getSpeed(self)[1]])
        if keys[pygame.K_s] and (self.playerrect.y < 300-self.playerrect.width):
            self.playerrect = self.playerrect.move([0,GameObject.GameObject.getSpeed(self)[1]])
    
    def updateCopterBlades(self):
        self.animationIndex = (self.animationIndex + 1) % len(self.copterBlades)
        self.copterBlade = self.copterBlades[self.animationIndex]        
        
    def getSpriteBlade(self):
        return self.copterBlade
    
    