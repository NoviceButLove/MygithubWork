import pygame
from alien import Alien


def create_alien(ai_settings,screen, aliens,alien_number,row_number):
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 创建第一行外星人
    # 创建一个外星人并将其加入当前行
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) -   ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_fleet(ai_settings,screen ,ship,aliens):
    '''创建外星人群'''
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    #创建第一行外星人
    number_rows = get_number_rows(ai_settings,ship.rect.height,
                                  alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,
                         row_number)

def regame(ai_settings,screen,ship,stats,aliens,bullets,sb):
    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    pygame.mouse.set_visible(False)
    # 清空外星人列表和子弹列表
    aliens.empty()
    bullets.empty()

    #重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # 创建一群新的外星人，并让飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
