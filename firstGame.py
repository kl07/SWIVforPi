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
        timer = 0
        debug = 1
        
        player = Player.Player(80, 250)  # First call module, then the class
        
        copterBlades = player.getSpriteBlade().get_rect()
        
        bullets = []
        enemies = []
                
        while 1:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullets.BasicBullet(player.rect.x+13, player.rect.y)
                        #soundObj = pygame.mixer.Sound('sfx/blast.wav')
                        #soundObj.play()
                        bullets.append(bullet)
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_q:
                        debug ^= 1
                        
            
            player.update(pygame.key.get_pressed())
            
            copterBlades.x = player.rect.x
            copterBlades.y = player.rect.y
            
            lblPosition = myfont.render("X:{0} Y:{1}".format(player.rect.x, player.rect.y), 1, (255,255,0))
            lblPosition2 = myfont.render("Bullets:{0}".format(len(bullets)), 1, (255,255,0))
            lblPosition3 = myfont.render("Time:{0}".format(timer), 1, (255,255,0))
            
            # Enemy AI Bounce behavior
            #if rect.left < 0 or rect.right > width:
            #    player.setSpeed(-player.getSpeed()[0], player.getSpeed()[1])
            #if rect.top < 0 or rect.bottom > height:
            #    player.setSpeed(player.getSpeed()[0], -player.getSpeed()[1]) 
                
            screen.fill(black)
            
            for bullet in bullets:                
                if(bullet.alive):
                    bullet.update()                    
                    screen.blit(bullet.getSprite(), bullet.rect)
                else:
                    bullets.remove(bullet)
            
            for enemy in enemies:
                if(enemy.alive):
                    screen.blit(enemy.getSprite(), enemy.rect)
                    enemy.update()
                    for bullet in bullets:
                        if(bullet.alive):
                            if(enemy.collision(bullet.rect.x, bullet.rect.y)):
                                bullets.remove(bullet)
                                enemy.alive = 0                                            
                else:
                    enemies.remove(enemy)
            
            if(debug):
                screen.blit(lblPosition, (5, 0))
                screen.blit(lblPosition2, (5, 12))
                screen.blit(lblPosition3, (5, 24))
            
            screen.blit(player.getSprite(), player.rect)
            
            screen.blit(player.getSpriteBlade(), copterBlades)
            pygame.display.flip()
            clock.tick(60)
            timer += 1
            
            if(timer == 200):
                enemies.append(Enemy.Enemy(30,0))
            elif(timer == 400):
                enemies.append(Enemy.Enemy(150,0))