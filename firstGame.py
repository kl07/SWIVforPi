import sys, pygame
from gameUnits import Player
from gameUnits import GameObject

pygame.init()

size = width, height = 600, 800
black = 0, 0, 0
screen = pygame.display.set_mode(size)

player = Player.Player(pygame.image.load("copter.gif").convert())  # First call module, then the class

print player.getSpeed()

ballrect = player.getSprite().get_rect()

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:    
                print "A pressed first time"                       
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        ballrect = ballrect.move([-1, 0])  
    if keys[pygame.K_d]:
        ballrect = ballrect.move([1, 0])
    if keys[pygame.K_w]:
        ballrect = ballrect.move([0,-1])  
    if keys[pygame.K_s]:
        ballrect = ballrect.move([0,1])            
        
        
    # Enemy AI Bounce behavior
    #if ballrect.left < 0 or ballrect.right > width:
    #    player.setSpeed(-player.getSpeed()[0], player.getSpeed()[1])
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    player.setSpeed(player.getSpeed()[0], -player.getSpeed()[1]) 
        
    screen.fill(black)
    screen.blit(player.getSprite(), ballrect)
    pygame.display.flip()