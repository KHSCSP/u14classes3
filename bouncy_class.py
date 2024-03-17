import pygame, random, math

class Bouncy:
    def __init__(self, x=100, y=100, size=10, col=None):
        self.x = x
        self.y = y
        
        self.xv = 0
        while self.xv == 0:
            self.xv = random.randint(-3, 3)
        
        self.yv = random.randint(-3, 3)
        self.size = size
        if col == None:
            self.color = Bouncy.rand_col()
        else:
            self.color = col

   
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    

    def move(self, screen):
        w, h = screen.get_size()
        if self.x < 0 or self.x > w:
            self.xv *= -1
        if self.y < 0 or self.y > h:
            self.yv *= -1
        self.x += self.xv
        self.y += self.yv


    def rand_move(self, screen):
        pass


    def tele_move(self, screen):
        pass


    # a helper function
    # *not a method* because no instance will call this
    # we will: Bouncy.rand_col()
    # we will *not*: b.rand_col()
    # it 'belongs' to the class, not an object 'itself'
    def rand_col():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)