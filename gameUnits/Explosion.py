'''
Created on Apr 2, 2014

@author: Kevin
'''
import pygame

class Explosion(object):

    def __init__(self, x, y):        
        self.animationIndex = 0
        self.alive = 1
        self.explosion = []
        self.explosion.append(pygame.image.load("images/ed1.gif"))
        self.explosion.append(pygame.image.load("images/ed2.gif"))
        self.explosion.append(pygame.image.load("images/ed3.gif"))
        self.explode = self.explosion[self.animationIndex]  
        self.clock = pygame.time.Clock()
        self.rect = self.explode.get_rect()
        self.rect.x = x
        self.rect.y = y         
    
    def update(self):
        if(self.animationIndex < 3): #make dynamic
            self.animationIndex += 1
            self.explode = self.explosion[self.animationIndex]
        else:
            self.alive = 0
    
    def getSprite(self):
        return self.explode
            
        