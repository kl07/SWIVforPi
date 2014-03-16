'''
Created on Mar 14, 2014

@author: Kevin
'''
import pygame
from gameUnits import GameObject

class Player(GameObject.GameObject):
      
    def __init__(self):
        super(Player, self).__init__("helicopter", [1, 1], pygame.image.load("images/copter.gif").convert())
        
        self.animationIndex = 0
        self.copterBlades = []
        self.copterBlades.append(pygame.image.load("images/copter_blade1.png"))
        self.copterBlades.append(pygame.image.load("images/copter_blade2.png"))
        self.copterBlades.append(pygame.image.load("images/copter_blade3.png"))
        
        self.copterBlade = self.copterBlades[self.animationIndex]
    
    def update(self):
        self.updateCopterBlades();
    
    def updateCopterBlades(self):
        self.animationIndex = (self.animationIndex + 1) % len(self.copterBlades)
        self.copterBlade = self.copterBlades[self.animationIndex]        
        
    def getSpriteBlade(self):
        return self.copterBlade
    
    