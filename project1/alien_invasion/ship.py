import pygame
from pygame.sprite import Sprite
#导入并继承
class Ship(Sprite):

    '''初始化飞船并设置其位置'''
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

    #加载飞船图像并获取其获取其外接矩形
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    #移动标志
        self.moving_right = False
        self.moving_left = False
        self.center = float(self.rect.centerx)
        self.center1 = float(self.rect.centery)
        self.moving_up = False
        self.moving_down = False


    def update(self):
        '''根据移动标志调整飞船的位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center1 -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < 800:
            self.center1 += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.centery = self.center1
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
















