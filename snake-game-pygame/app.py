import pygame
from pygame.locals import *

pygame.init() #sempre que usar o pygame precisamos iniciá-lo

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = pygame.

while True:
    
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
        
    pygame.display.update()