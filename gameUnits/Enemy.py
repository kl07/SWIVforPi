'''
Created on Apr 1, 2014

@author: Kevin
'''
import pygame

from gameUnits import GameObject

class Enemy(GameObject.GameObject):
      
    def __init__(self, x, y, id):
        if(id==1):
            super(Enemy, self).__init__("beetle ship", [1, 3], pygame.image.load("images/e1.gif").convert(), x, y)
            self.hp = 2
            self.score = 25
        elif(id==2):    
            super(Enemy, self).__init__("battle cruiser", [1, 1], pygame.image.load("images/c1.gif").convert(), x, y)
            self.hp = 21
            self.score = 400
            
        self.id = id
          
        
    def update(self):
        if(self.hp <= 0):
            self.alive = 0
        else:
            self.rect = self.rect.move([0,GameObject.GameObject.getSpeed(self)[1]])        
        
    def collision(self, bulletX, bulletY):
        return (bulletX > self.rect.x and bulletX < self.rect.x + self.rect.width and bulletY > self.rect.y and bulletY < self.rect.y + self.rect.height)