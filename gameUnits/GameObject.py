'''
Created on Mar 14, 2014

@author: Kevin
'''
class GameObject(object):

    def __init__(self, name, speed, sprite):
        self.name = name
        self.speed = speed
        self.sprite = sprite
        
    def getName(self):
        return self.name
    
    def getSpeed(self):
        return self.speed
    
    def getSprite(self):
        return self.sprite
        
    def setSpeed(self, x, y):
        self.speed = [x, y]