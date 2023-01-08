import pygame
from pygame.locals import *
import random

# 创建一个 球类
class Ball():
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.image.load('images/ball.png')
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # 随机出发
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # 随机速度，随机方向
        speedList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedList)
        self.ySpeed = random.choice(speedList)

    def update(self):
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        self.x += self.xSpeed
        self.y += self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))


