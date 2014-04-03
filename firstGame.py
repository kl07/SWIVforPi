import sys, pygame
import Joystick
import random

from gameUnits import Player
from gameUnits import Enemy
from gameUnits import Explosion
from projectiles import Bullets
from threading import Thread
    
class SwivPi(object):     
    
    def main(self):
        pygame.init() 
        pygame.display.set_caption("SWIV for Pi")
        #pygame.mixer.init()
        bg1 = pygame.image.load("images/bg1.gif")
        title = pygame.image.load("images/title.gif")
        tx1 = pygame.image.load("images/text1.gif")        
        
        #bgm = "sfx/bmlevel1.mid"
        #pygame.mixer.music.load(bgm)
        
        clock = pygame.time.Clock()
        size = width, height = 200, 300    
        screen = pygame.display.set_mode(size)
        myfont = pygame.font.SysFont("monospace", 11)
        timer = 0
        debug = 0
        score = 0
        buttonPressed = 0
        gameOver = 1
        deathCounter = 0
        
        player = Player.Player(80, -100)  # First call module, then the class
        
        copterBlades = player.getSpriteBlade().get_rect()
        
        bullets = []
        enemies = []
        deaths = []
        
        #pygame.mixer.music.play()
        
        js = Joystick.Joystick()            
        js.main()          
         
        while(gameOver):
            joyButton = 700#js.readadc(2, js.SPICLK, js.SPIMOSI, js.SPIMISO, js.SPICS)
            if(joyButton > 1000):
                gameOver = 0                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    js.deactivateLED() 
                    sys.exit()      
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameOver = 0                        
                    elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        js.deactivateLED()
                        sys.exit()
            screen.blit(bg1, (0, 0))
            screen.blit(title, (25, 20))
            screen.blit(tx1, (40, 120))
            pygame.display.flip()
            clock.tick(60)
        
        #activate the game
        player.rect.y = 250
        js.deactivateLED()
        
        while (deathCounter < 50):            
            joyX = js.readadc(1, js.SPICLK, js.SPIMOSI, js.SPIMISO, js.SPICS)
            joyY = js.readadc(0, js.SPICLK, js.SPIMOSI, js.SPIMISO, js.SPICS)
            joyButton = js.readadc(2, js.SPICLK, js.SPIMOSI, js.SPIMISO, js.SPICS)
            
            #print("X:{0} Y:{1} B:{2}".format(joyX, joyY, joyButton))     
            
            if(joyButton > 1000 and buttonPressed == 0):
                bullet = Bullets.BasicBullet(player.rect.x+13, player.rect.y)
                bullets.append(bullet)
                buttonPressed = 1
                js.setLED(1, True)
            else:
                buttonPressed = 0
                js.setLED(1, False)            
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    js.deactivateLED()
                    sys.exit()      
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullets.BasicBullet(player.rect.x+13, player.rect.y)
                        #soundObj = pygame.mixer.Sound('sfx/blast.wav')
                        #soundObj.play()
                        bullets.append(bullet)
                    elif event.key == pygame.K_ESCAPE:
                        js.deactivateLED()
                        sys.exit()
                    elif event.key == pygame.K_e:
                        debug ^= 1
                        
            
            player.update(pygame.key.get_pressed(), joyX, joyY)
            
            copterBlades.x = player.rect.x
            copterBlades.y = player.rect.y
            
            lblPosition = myfont.render("X:{0} Y:{1}".format(player.rect.x, player.rect.y), 1, (0,0,0))
            lblPosition2 = myfont.render("Bullets:{0}".format(len(bullets)), 1, (0,0,0))
            lblPosition3 = myfont.render("Time:{0}".format(timer), 1, (0,0,0))
            lblScore = myfont.render("score:{0}".format(score), 1, (255,255,255))
            
            # Enemy AI Bounce behavior
            #if rect.left < 0 or rect.right > width:
            #    player.setSpeed(-player.getSpeed()[0], player.getSpeed()[1])
            #if rect.top < 0 or rect.bottom > height:
            #    player.setSpeed(player.getSpeed()[0], -player.getSpeed()[1]) 
            
            
            # Start drawing
            screen.blit(bg1, (0, 0))
                        
            for bullet in bullets:                
                if(bullet.alive):
                    bullet.update()                    
                    screen.blit(bullet.getSprite(), bullet.rect)
                else:
                    bullets.remove(bullet)
            
            for enemy in enemies:
                if(enemy.alive):
                    if (player.collision(enemy.rect.x, enemy.rect.x+enemy.rect.width, enemy.rect.y, enemy.rect.y + enemy.rect.height)):
                        if(enemy.id != 2):
                            enemy.alive = 0                            
                    screen.blit(enemy.getSprite(), enemy.rect)
                    enemy.update()                    
                    for bullet in bullets:
                        if(bullet.alive):
                            if(enemy.collision(bullet.rect.x, bullet.rect.y)):
                                bullets.remove(bullet)
                                enemy.hp -= 1
                                                                            
                else:
                    deaths.append(Explosion.Explosion(enemy.rect.x, enemy.rect.y, enemy.id))
                    score += enemy.score
                    enemies.remove(enemy)
                if(enemy.rect.y > 350):
                    enemies.remove(enemy)
            
            for explosion in deaths:
                if(explosion.alive):
                    explosion.update()
                    screen.blit(explosion.getSprite(), explosion.rect)
                else:
                    deaths.remove(explosion)
                
            if(debug):
                screen.blit(lblPosition, (5, 0))
                screen.blit(lblPosition2, (5, 12))
                screen.blit(lblPosition3, (5, 24))
            
            if(player.alive):
                screen.blit(player.getSprite(), player.rect)            
                screen.blit(player.getSpriteBlade(), copterBlades)
            else:                
                deaths.append(Explosion.Explosion(player.rect.x, player.rect.y, 0))
                player.rect.y = -100
                gameOver = 1
            
            #display score
            screen.blit(lblScore, (5, 288))
            
            if(gameOver):
                deathCounter += 1
                screen.blit(title, (25, 20))
                screen.blit(tx1, (40, 120))
                js.setLED(2, True)
                
            pygame.display.flip()
            clock.tick(60)
            timer = (timer+1)%50000
            
            if(timer%1000 == 0):
                enemies.append(Enemy.Enemy(50,-200,2))
            elif(timer%200 == 0):
                enemies.append(Enemy.Enemy(random.randint(20,180),0,1))
            elif(timer%350 == 0):
                enemies.append(Enemy.Enemy(random.randint(20,180),0,1))
            elif(timer%67 == 0):
                enemies.append(Enemy.Enemy(random.randint(20,180),0,1))
        
        #while done, gameOver
        self.main()