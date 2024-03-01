import pygame, sys, random
from pygame.locals import QUIT
from bouncy_class import Bouncy

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')

# define a few bouncy objects



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