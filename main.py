from random import randint

import pygame

pygame.init()

pygame.display.set_caption("Fun Bounce Game for Boys and Girls")
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen = pygame.display.set_mode((800, 600))

x = 400
y = 100
rany = randint(0, 500)
ranx = randint(0, 750)
velocity = 0
acceleration = 0.1
running = True
xvelocity = 5
minvel = -6
jumps = 5

font = pygame.font.Font(None, 60)

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jumps > 0:
                    velocity = minvel
                    jumps -= 1
        if event.type == pygame.QUIT:
            running = False
    pygame.init()
    if x == 700:
        xvelocity = -5
    elif x == 0:
        xvelocity = 5
    if y >= 550:
        running = False
    elif y <= 0:
        velocity = 3
    x += xvelocity
    velocity += acceleration
    y += velocity
    screen.fill(white)
    rect = pygame.draw.rect(screen, blue, (x, y, 100, 50))
    ransquare = pygame.draw.rect(screen, red, (ranx, rany, 50, 50))
    if rect.colliderect(ransquare):
        ranx = randint(0, 750)
        rany = randint(0, 500)
        jumps += 1
    text = font.render(str(jumps), True, black, None)
    screen.blit(text, (10, 10))
    pygame.display.update()
    pygame.time.delay(10)
#
