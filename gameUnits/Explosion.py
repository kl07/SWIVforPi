'''
Created on Apr 2, 2014

@author: Kevin
'''
import sys
import pygame

class Explosion(object):

    def __init__(self, x, y, id):        
        self.animationIndex = 0
        self.alive = 1
        self.explosion = []
        if(id == 1): #first because most common enemy
            self.explosion.append(pygame.image.load("images/ed1.gif"))
            self.explosion.append(pygame.image.load("images/ed1.gif"))
            self.explosion.append(pygame.image.load("images/ed2.gif"))
            self.explosion.append(pygame.image.load("images/ed2.gif"))
            self.explosion.append(pygame.image.load("images/ed3.gif"))
            self.explosion.append(pygame.image.load("images/ed3.gif"))
        elif(id == 0): #player
            self.explosion.append(pygame.image.load("images/pd1.gif"))
            self.explosion.append(pygame.image.load("images/pd1.gif"))
            self.explosion.append(pygame.image.load("images/pd2.gif"))
            self.explosion.append(pygame.image.load("images/pd2.gif"))
            self.explosion.append(pygame.image.load("images/pd3.gif"))
            self.explosion.append(pygame.image.load("images/pd3.gif"))
        elif(id == 2): # battle cruiser
            self.explosion.append(pygame.image.load("images/cd1.gif"))
            self.explosion.append(pygame.image.load("images/cd1.gif"))
            self.explosion.append(pygame.image.load("images/cd1.gif"))
            self.explosion.append(pygame.image.load("images/cd1.gif"))
            self.explosion.append(pygame.image.load("images/cd2.gif"))
            self.explosion.append(pygame.image.load("images/cd2.gif"))
            self.explosion.append(pygame.image.load("images/cd2.gif"))
            self.explosion.append(pygame.image.load("images/cd2.gif"))
            self.explosion.append(pygame.image.load("images/cd3.gif"))
            self.explosion.append(pygame.image.load("images/cd3.gif"))
            self.explosion.append(pygame.image.load("images/cd3.gif"))            
            self.explosion.append(pygame.image.load("images/cd4.gif"))
            self.explosion.append(pygame.image.load("images/cd4.gif"))
            self.explosion.append(pygame.image.load("images/cd4.gif"))
            self.explosion.append(pygame.image.load("images/cd4.gif"))
            self.explosion.append(pygame.image.load("images/cd4.gif"))
            
        self.explode = self.explosion[self.animationIndex]       
        self.rect = self.explode.get_rect()
        self.rect.x = x
        self.rect.y = y         
    
    def update(self):
        if(self.animationIndex < len(self.explosion)):                     
            self.explode = self.explosion[self.animationIndex]
            self.animationIndex += 1            
        else:
            self.alive = 0
    
    def getSprite(self):
        return self.explode
            
        