import pygame, random, math

class Bouncy:
    def __init__(self, x=100, y=100, size=10):
        pass
    
    def draw(self, screen):
        pass
    

    def move(self, screen):
        pass
    
    def rand_move(self, screen):
        pass

    def tele_move(self, screen):
        pass


    # a helper function
    # not a method because no instance will call this
    def rand_col():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)