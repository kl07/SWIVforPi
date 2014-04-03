'''
Created on Apr 1, 2014

@author: Kevin
'''
import pygame

from gameUnits import GameObject

class Enemy(GameObject.GameObject):
      
    def __init__(self, x, y):
        super(Enemy, self).__init__("beetle ship", [1, 1], pygame.image.load("images/e1.gif").convert(), x, y)  
        
    def update(self):
        self.rect = self.rect.move([0,GameObject.GameObject.getSpeed(self)[1]])
        
    def collision(self, bulletX, bulletY):
        return (bulletX > self.rect.x and bulletX < self.rect.x + self.rect.width and bulletY > self.rect.y and bulletY < self.rect.y + self.rect.height)