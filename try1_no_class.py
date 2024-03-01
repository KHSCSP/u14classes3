import pygame, sys
from pygame.locals import QUIT

w = 800
h = 600
pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')

# TODO initial values for position, size, and velocity
x1 = 100
y1 = 100
size1 = 10
xV1 = 3
yV1 = -2
col1 = (0,255,0)


# TODO variables for the second and third bouncy shapes


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255,255,255))
    
    # TODO if hit edge, bounce
    if x1 < 0 or x1 > w:
        xV1 *= -1
    if y1 < 0 or y1 > h:
        yV1 *= -1

    # TODO move
    x1 += xV1
    y1 += yV1

    # TODO draw the circle
    pygame.draw.circle(screen, col1, (x1,y1), size1)

    
    # TODO second and third shapes: bounce, move, draw
    
    
    # slow it down a bit
    pygame.display.update()
    pygame.time.delay(5)
  