'''
Created on Mar 14, 2014

@author: Kevin
'''
import pygame
from gameUnits import GameObject

class Player(GameObject.GameObject):
      
    def __init__(self):
        super(Player, self).__init__("helicopter", [1, 1], pygame.image.load("images/p1.gif").convert())
        
        self.animationIndex = 0
        self.copterBlades = []
        self.copterBlades.append(pygame.image.load("images/b1.gif"))
        self.copterBlades.append(pygame.image.load("images/b2.gif"))
        self.copterBlades.append(pygame.image.load("images/b3.gif"))
        
        self.copterBlade = self.copterBlades[self.animationIndex]
    
    def update(self):
        self.updateCopterBlades();
    
    def updateCopterBlades(self):
        self.animationIndex = (self.animationIndex + 1) % len(self.copterBlades)
        self.copterBlade = self.copterBlades[self.animationIndex]        
        
    def getSpriteBlade(self):
        return self.copterBlade
    
    