import pygame
#from pygame.locals import *
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from Boyfriend import Alien

#gf.test()

def run():
    
    pygame.init()
    #
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
   
    pygame.display.set_caption("Boyfriend Invasion")

    # 创建一个飞船
    ship = Ship(ai_settings, screen)
    # 子弹组
    bullets = Group()
    # 外星人
    alien = Alien(ai_settings, screen)
    #background_color
    bg_color = ai_settings.bg_color

    while True:
        gf.check_events(ship, screen, ai_settings, bullets)
        ship.upadte()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, alien)

                 

#
run()                