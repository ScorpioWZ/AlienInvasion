import pygame
from pygame.locals import *

def run_game():
    pygame.init()
    screen = pygame.display.set_mode(("1200,800"))
    #pygame.display.set_caption('Alien Invation')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
run_game()                