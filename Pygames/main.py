import pygame
from player import Player
import glob
from pygame.locals import *


width = 1250
height = 800
FPS = 60
screen = pygame.display.set_mode ((width,height))
pygame.display.set_caption ("hagra adventure")
background = pygame.image.load("images/newbg.png").convert()
animation  =   []
for i in range(1, 15):
    animation.append(pygame.image.load('images/Idle ('+str(i)+').png').convert_alpha())
    image = pygame.image.load(f'images/Idle ({i}).png')
    image = pygame.transform.scale(image, (150, 150))
# image = animation[0]
# rect    =   image.get_rect()


IsPlayer =  Player(500,500,screen)


def Draw(x,y):

    screen.blit(image,(x,y))   
    # pygame.draw.circle(self.screen, (0, 0, 255), (self.x, self.y), 75)
    # Run until the user asks to quit
    x   =   (width * 0.45 )
    y   =   (height * 0.8)

def update():
    if count == len(animation):
        count = 0
    image = animation[count]
    count += 1

    
running = True
while running:
    IsPlayer.update()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_h:
                IsPlayer.Dep()
        elif event.type == pygame.QUIT:
            running = False
            screen = pygame.display.set_mode(
            event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
    # Fill the background with white
    screen.fill((255, 255, 255))
    screen.blit(pygame.transform.scale(background,size=(1250,800)), (0, 0))
    Draw(10,30)
    
    pygame.display.update()

    

    # Flip the display
    pygame.display.flip()
  