import pygame as pg, sys
from pygame.locals import *
import random, time

pg.init()

FramePerSec = pg.time.Clock()
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0


# Fonts
font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Background atributes 
background = pg.image.load(r"AnimatedStreet.png")
pg.mixer.music.load(r'background.wav')
pg.mixer.music.play()

# Creating of screen
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Racer')

# MAIN
class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, 500)
    
    def move(self):
        pressed_keys = pg.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -SPEED)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_s]:
                self.rect.move_ip(0, SPEED)
        if self.rect.left > 0:
            if pressed_keys[K_a]:
                self.rect.move_ip(-SPEED, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_d]:
                self.rect.move_ip(SPEED, 0)           

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
    
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r"Coin.png")
        self.image = pg.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(80, SCREEN_WIDTH-80), random.randint(SCREEN_HEIGHT/2, SCREEN_HEIGHT))


Enemy = Enemy()
Player = Player()
Coin = Coin()


#Creating Sprites Groups
enemies = pg.sprite.Group()
coins = pg.sprite.Group()
coins.add(Coin)
enemies.add(Enemy)
all_sprites = pg.sprite.Group()
all_sprites.add(Player)
all_sprites.add(Enemy)


#Adding a new User event 
INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 1000)

# BODY
while True:
    for event in pg.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    SCREEN.blit(background, (0,0))
    scores = font_small.render(f'Score:{SCORE}', True, BLACK)
    coin_display = font_small.render(f'Coins:{COINS}', True, BLACK)
    SCREEN.blit(scores, (10,0))
    SCREEN.blit(coin_display, (10,20))
    SCREEN.blit(Coin.image, Coin.rect)
    

    # Re-draw of sprites and their movement
    for sprite in all_sprites:
        sprite.move()
        SCREEN.blit(sprite.image, sprite.rect)

    if pg.sprite.spritecollideany(Player, enemies):
          pg.mixer.Sound(r'crash.wav').play()
          time.sleep(1)
          while True:
            SCREEN.fill(WHITE)
            SCREEN.blit(game_over, (30,250))
            SCREEN.blit(scores, (40,320))
            SCREEN.blit(coin_display, (200,320))
            pg.display.update()
            for sprite in all_sprites:
                    sprite.kill() 
            for event in pg.event.get():   
                    if event.type == QUIT:
                        pg.quit()
                        sys.exit()

    if pg.sprite.spritecollideany(Player, coins):
        Coin.rect.center = (random.randint(80, SCREEN_WIDTH-80), random.randint(SCREEN_HEIGHT/2, SCREEN_HEIGHT))
        COINS += 1

    pg.display.update()
    FramePerSec.tick(60)