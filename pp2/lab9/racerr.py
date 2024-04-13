import random
import pygame 

# Initializing 
pygame.init()

# Screen 
WIDTH = 400
HEIGHT = 600
SURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street Racer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

# Background 
bg = pygame.image.load("pp2/lab9/AnimatedStreet.png")

# Font 
score_font = pygame.font.SysFont("Verdana", 50)
big_font = pygame.font.SysFont("Verdana", 70)
rest_font = pygame.font.SysFont("Verdana", 50)
restart = rest_font.render("Press R to restart", True, BLACK)
game_over = big_font.render("GAME OVER", True, BLACK)

# Variables 
paused = False
STEP = 5
SCORE = 0
COIN_WEIGHTS = [1, 2, 3]  # Different weights for coins
N_COINS_TO_SPEED_UP = 10  # Number of coins to earn before speeding up enemies

# Classes 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pp2/lab9/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pp2/lab9/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def update(self):
        self.rect.move_ip(0, STEP)
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        weight = random.choice(COIN_WEIGHTS)
        self.image = pygame.transform.scale(pygame.image.load(f"pp2/lab9/Coin(1){weight}.png"), (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), -200)

    def update(self):
        self.rect.move_ip(0, STEP)
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), -200)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


def game_over_screen():
    global paused
    while paused:
        clock.tick(5)
        SURF.fill(RED)
        SURF.blit(game_over, (30, 250))
        SURF.blit(restart, (55, 300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    global STEP
                    global SCORE
                    STEP = 5
                    SCORE = 0
                    paused = False
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()


def main():
    global STEP, SCORE
    STEP = 5
    SCORE = 0

    P1 = Player()
    E1 = Enemy()
    C1 = Coin()

    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    enemies.add(E1)
    coins.add(C1)

    pygame.mixer.music.load("pp2/lab9/wwww.wav")
    pygame.mixer.music.play(-1)

    running = True

    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == INC_SPEED:
                STEP += 0.3
            if SCORE >= N_COINS_TO_SPEED_UP:
                STEP += 0.5  # Increase enemy speed

        P1.update()
        for enemy in enemies:
            enemy.update()
        C1.update()

        if pygame.sprite.spritecollideany(P1, enemies):
            pygame.mixer.music.pause()
            pygame.mixer.Sound("pp2/lab9/crash.wav").play()
            global paused
            paused = True
            game_over_screen()
            for enemy in enemies:
                enemy.kill()

        if pygame.sprite.spritecollideany(P1, coins):
            SCORE += 1
            pygame.mixer.Sound("pp2/lab9/Coin.mp3").play()
            for c in coins:
                c.kill()
            C1 = Coin()
            coins.add(C1)

        SURF.blit(bg, (0, 0))

        for enemy in enemies:
            enemy.draw(SURF)
        P1.draw(SURF)
        C1.draw(SURF)
        score_img = score_font.render(str(SCORE), True, BLACK)
        SURF.blit(score_img, (10, 10))

        if SCORE == 10 and len(enemies) < 2:
            E = Enemy()
            enemies.add(E)

        pygame.display.update()

    pygame.quit()
    exit()

main()
