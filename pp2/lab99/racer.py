import random 
import pygame 
 
# Инициализация
pygame.init() 
 
# Экран
WIDTH = 400 
HEIGHT = 600 
SURF = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Street Racer") 
 
# Цвета
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
PINK = (255, 192, 203) 

GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
 
clock = pygame.time.Clock() 
 
# Фон
bg = pygame.image.load("pp2/lab99/AnimatedStreet.png") 
 
# Шрифты
score_font = pygame.font.SysFont("Roboto-Bold.ttf", 50, True, True) 
big_font = pygame.font.SysFont("Roboto-Bold.ttf", 70, True, False) 
rest_font = pygame.font.SysFont("Roboto-Bold.ttf", 50, False, False) 
restart = rest_font.render("Press R to restart", True, BLACK) 
game_over = big_font.render("GAME OVER", True, BLACK) 
 
# Переменные
paused = False 
STEP = 5 
SCORE = 0  # Добавлено для сохранения счета

class Player(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.image.load("pp2/lab99/Player.png") 
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
        self.image = pygame.image.load("pp2/lab99/Enemy.png") 
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(40, WIDTH - 40), 0) 
 
    def update(self): 
        self.rect.move_ip(0, STEP) 
        if self.rect.top > HEIGHT: 
            self.rect.center = (random.randint(30, 350), 0) 
 
    def draw(self, surface): 
        surface.blit(self.image, self.rect) 
 
class Coin(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("pp2/lab99/Coin.png"), (40, 40)) 
        self.image2 = pygame.transform.scale(pygame.image.load("pp2/lab99/coin3.png"), (40, 40)) 
        self.rect = self.image.get_rect() 
        self.rect2 = self.image2.get_rect() 
        self.rect.center = (random.randint(40, WIDTH - 40), -200) 
        self.rect2.center = (random.randint(40, WIDTH - 40), -200) 
 
    def update(self): 
        self.rect.move_ip(0, STEP) 
        if self.rect.top > HEIGHT: 
            self.rect.center = (random.randint(40, WIDTH - 40), -200) 
 
        self.rect2.move_ip(0, STEP) 
        if self.rect2.top > HEIGHT: 
            self.rect2.center = (random.randint(40, WIDTH - 40), -200) 
 
    def draw(self, surface): 
        surface.blit(self.image, self.rect) 
        surface.blit(self.image2, self.rect2) 
 
def fgame_over(): 
    global paused 
    while paused: 
        clock.tick(5) 
        SURF.fill(PINK) 
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
    global STEP 
    global SCORE  # Добавлено для сохранения счета
    STEP = 5 
    SCORE = 0 
 
    P1 = Player() 
    E1 = Enemy() 
    C1 = Coin() 
 
    enemies = pygame.sprite.Group() 
    coins = pygame.sprite.Group() 
    enemies.add(E1) 
    coins.add(C1) 
 
    pygame.mixer.music.load("pp2/lab99/wwww.wav") 
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
 
        P1.update() 
        for enemy in enemies: 
            enemy.update() 
        C1.update() 
 
        if pygame.sprite.spritecollideany(P1, enemies): 
            pygame.mixer.music.pause() 
            pygame.mixer.Sound("pp2/lab99/crash.wav").play() 
            global paused 
            paused = True 
            fgame_over() 
            for enemy in enemies: 
                enemy.kill() 
 
        if pygame.sprite.spritecollideany(P1, coins): 
            SCORE += 1 
            pygame.mixer.Sound("pp2/lab99/Coin.mp3").play() 
 
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
