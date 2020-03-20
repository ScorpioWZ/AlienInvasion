import pygame

class Ship():

    def __init__(self, ai_settings, screen):

        self.screen = screen
        self.ai_settings = ai_settings
        

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # 获取飞船的矩形
        
        self.screen_rect = screen.get_rect() #获取屏幕的矩形
        
        #飞船中心的x = 屏幕中心的x
        self.rect.centerx = self.screen_rect.centerx
        #飞船 放到 屏幕矩形的底部
        self.rect.bottom = self.screen_rect.bottom

        #飞船的属性 center
        self.center = float(self.rect.centerx)
        
        #右移
        self.moving_right = False
        #左移
        self.moving_left = False

             
    def upadte(self):
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and (self.rect.left > 0):
            self.center -= self.ai_settings.ship_speed_factor

        #更新rect
        self.rect.centerx = self.center   


    def blitme(self):
        self.screen.blit(self.image, self.rect)    


