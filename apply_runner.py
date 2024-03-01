# TODO
# create a new class (the X shape, or crosshair, or something else)
# use any type of motion for your objects
# animate at least 3 of your objects

import pygame, sys, random
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # -------- end event loop
    screen.fill((255,255,255))

    
    # move and draw
 

    

    pygame.display.update()
    pygame.time.delay(2)