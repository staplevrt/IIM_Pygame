
import pygame
from glob import glob


class Player(pygame.sprite.Sprite):

    def __init__(self,x,y,screen):
        super().__init__()
        self.animation = []
        for i in range(1, 15):
            self.animation.append(pygame.image.load('images/Idle ('+str(i)+').png').convert_alpha())
        self.image = self.animation[0]
        self.rect = self.image.get_rect()
        self.count = 0
        self.y = y
        self.x  = x
        self.screen = screen
    
    def update(self):

        if self.count == len(self.animation):
            self.count = 0
            self.image = self.animation[self.count]
        
        self.count += 1
        

    def Deplacement(self,x,y):

        self.x+=x
        self.y+=y

# g = pygame.sprite.Group()
"""sprite = Player()
g.add(sprite)
print(sprite)""" 