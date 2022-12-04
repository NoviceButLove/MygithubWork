import pygame

class Player_images():

    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/bg1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def drew_myplayer(self):
        self.screen.blit(self.image,self.screen_rect)


