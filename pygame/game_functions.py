import pygame
from pygame.locals import *
from bullet import Bullet
from Boyfriend import Alien
import sys

def check_keydown_event(event, ship, ai_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ship, ai_settings, screen, bullets)
    elif event.key == pygame.K_q:
        sys.exit()    

               
    
def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship, ai_settings, screen, bullets):

    for event in pygame.event.get():
        #退出程序
            if event.type == QUIT:
                exit()
                #键盘按下
            elif event.type == pygame.KEYDOWN:
                check_keydown_event(event, ship, screen, ai_settings, bullets)
                #键盘抬起
            elif event.type == pygame.KEYUP:
                check_keyup_event(event, ship)

def fire_bullet(ship, ai_settings, screen, bullets):

    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

      

def update_screen(ai_settings, screen, ship, bullets, alien):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.blitme()
    pygame.display.flip()   

     
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

