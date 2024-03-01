import pygame, sys, random
from pygame.locals import QUIT
from bouncy_class import Bouncy

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

# define a few bouncy objects
# some will bounce off walls
# some will 'teleport'
# some will move randomly



# we'll use this later...(for random motion)
ticks = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # -------- end event loop
    screen.fill((255,255,255))
    ticks += 1
    
    # move and draw
    

    if ticks >= 1000:
        ticks = 0

    pygame.display.update()
    pygame.time.delay(2)