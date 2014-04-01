import sys, pygame

from gameUnits import Player
from gameUnits import Enemy
from projectiles import Bullets
    
class SwivPi(object):     
    
    def main(self):
        pygame.init() 
        pygame.mixer.init()
        
        clock = pygame.time.Clock()
        size = width, height = 200, 300
        black = 20, 20, 200
        screen = pygame.display.set_mode(size)
        myfont = pygame.font.SysFont("monospace", 11)
        
        player = Player.Player()  # First call module, then the class
        player.playerrect.x = 80
        player.playerrect.y = 250
        copterBlades = player.getSpriteBlade().get_rect()
        
        enemy= Enemy.Enemy()
        enemy.rect.x = 50          
        
        bullets = []
        
        while 1:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullets.BasicBullet(player.playerrect.x+13, player.playerrect.y)
                        soundObj = pygame.mixer.Sound('sfx/blast.wav')
                        soundObj.play()
                        bullets.append(bullet)
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()
                        
            
            player.update(pygame.key.get_pressed())
            
            if(enemy.alive):
                enemy.update()
            
            copterBlades.x = player.playerrect.x
            copterBlades.y = player.playerrect.y
            
            lblPosition = myfont.render("X:{0} Y:{1}".format(player.playerrect.x, player.playerrect.y), 1, (255,255,0))
            lblPosition2 = myfont.render("Bullets:{0}".format(len(bullets)), 1, (255,255,0))
            
            # Enemy AI Bounce behavior
            #if playerrect.left < 0 or playerrect.right > width:
            #    player.setSpeed(-player.getSpeed()[0], player.getSpeed()[1])
            #if playerrect.top < 0 or playerrect.bottom > height:
            #    player.setSpeed(player.getSpeed()[0], -player.getSpeed()[1]) 
                
            screen.fill(black)
            
            for bullet in bullets:
                if(bullet.alive):
                    if(enemy.collision(bullet.rect.x, bullet.rect.y)):
                        bullets.remove(bullet)
                        enemy.alive = 0
                    bullet.update()
                    screen.blit(bullet.getSprite(), bullet.rect)
                else:
                    bullets.remove(bullet)
                    
            screen.blit(lblPosition, (5, 0))
            screen.blit(lblPosition2, (5, 12))
            
            screen.blit(player.getSprite(), player.playerrect)
            if(enemy.alive):
                screen.blit(enemy.getSprite(), enemy.rect)
            
            screen.blit(player.getSpriteBlade(), copterBlades)
            pygame.display.flip()
            clock.tick(60)           
