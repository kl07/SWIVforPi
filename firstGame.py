import sys, pygame

from gameUnits import Player
from gameUnits import GameObject
    
class SwivPi(object):     
    
    def main(self):
        pygame.init() 
        clock = pygame.time.Clock()
        size = width, height = 200, 300
        black = 0, 255, 0
        screen = pygame.display.set_mode(size)
        myfont = pygame.font.SysFont("monospace", 11)
        
        player = Player.Player()  # First call module, then the class
        
        ballrect = player.getSprite().get_rect()
        copterBlades = player.getSpriteBlade().get_rect()
        
        while 1:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:    
                        print "FIRE"               
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()           
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                ballrect = ballrect.move([-player.getSpeed()[0], 0])
            if keys[pygame.K_d]:
                ballrect = ballrect.move([player.getSpeed()[0], 0])
            if keys[pygame.K_w]:
                ballrect = ballrect.move([0,-player.getSpeed()[1]])
            if keys[pygame.K_s]:
                ballrect = ballrect.move([0,player.getSpeed()[1]])
            
            player.update()
            copterBlades.x = ballrect.x
            copterBlades.y = ballrect.y
            
            
            lblPosition = myfont.render("X:{0} Y:{1}".format(ballrect.x, ballrect.y), 1, (255,255,0))
            
            
            # Enemy AI Bounce behavior
            #if ballrect.left < 0 or ballrect.right > width:
            #    player.setSpeed(-player.getSpeed()[0], player.getSpeed()[1])
            #if ballrect.top < 0 or ballrect.bottom > height:
            #    player.setSpeed(player.getSpeed()[0], -player.getSpeed()[1]) 
                
            screen.fill(black)
            screen.blit(lblPosition, (5, height-12))
            screen.blit(player.getSprite(), ballrect)
            
            screen.blit(player.getSpriteBlade(), copterBlades)
            pygame.display.flip()
            clock.tick(60)           
