'''
Created on Mar 14, 2014

@author: Kevin
'''
from gameUnits import GameObject

class Player(GameObject.GameObject):

    def __init__(self, sprite):
        super(Player, self).__init__("helicopter", [1, 1], sprite)