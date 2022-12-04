import sys

import game_functions as gf
from settings import Settings#导入自定义设置模块
import pygame
from ship import Ship
from  player_background import Player_images as pli
from pygame.sprite import  Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreborad

'''class AlineInvasion:
    def __init__(self)  :
        pygame.init()
'''


def run_game():
    '''启动游戏'''

    #设置背景色
    #bg_color = (230,230,230)
    # 创建设置类的实例对象
    ai_setting = Settings()
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))#设置屏幕尺寸

    bg_player = pli(screen)
    pygame.display.set_caption("Alien Invasion")#设置窗口题目
    #创建一艘飞船
    ship = Ship(ai_setting,screen)
    alien = Alien(ai_setting,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()
    gf.create_fleet(ai_setting,screen,ship,aliens)

    stats = GameStats(ai_setting)#创建实例对象
    sb = Scoreborad(ai_setting,screen,stats)
    play_button = Button(ai_setting,screen,'Play')

    #读取历史最高分


    #开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_setting,screen,stats,play_button,ship,aliens,bullets,sb)
        if stats.game_active :
            ship.update()
            gf.update_bullets(ai_setting,screen,stats,sb,ship,aliens,bullets)
            #print(len(bullets))用于查看子弹剩余数量，占内存
            gf.update_aliens(ai_setting,stats,screen,ship,aliens,bullets,sb)
        #每次循环重绘屏幕
        # 刷新屏幕
        gf.update_screen(ai_setting,screen,stats,sb,ship,bullets,aliens,bg_player,play_button)

if __name__ == '__main__':
    run_game()