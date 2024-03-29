import pygame

pygame.init()
screen = pygame.display.set_mode((500, 400))
done = False
is_blue = True
while not done:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))
        if event.type == pygame.QUIT:
                        done = True
if is_blue: color = (0, 128, 255)
else: color = (255, 100, 0)
pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

pygame.display.flip()

if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    is_blue = not is_blue