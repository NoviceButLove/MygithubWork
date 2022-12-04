import sys

import pygame
import start_game
from bullet import Bullet
from alien import Alien
from time import sleep
from start_game import create_fleet
from start_game import regame


def check_events(ai_settings,screen,stats,button,ship,aliens,bullets,sb):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,button,ship,aliens,bullets,sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
            if button_clicked and not stats.game_active:
                regame(ai_settings, screen, ship,stats, aliens, bullets,sb)

def check_keydown_events(event,ai_settings,screen,stats,button,ship,aliens,bullets,sb):
    #移动飞机
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    #发射子弹
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    #按P进入游戏
    elif event.key == pygame.K_p:
        if not stats.game_active:
            ai_settings.initialize_dynamic_settings()
            regame(ai_settings, screen, ship,stats, aliens, bullets,sb)
    #按Q退出游戏
    elif event.key == pygame.K_q:

        sys.exit()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False

def update_screen(ai_settings,screen,stats,scoreborad,ship,bullets,aliens,bg_player,button):
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    '''
    对编组调用draw()，Pygame自动绘制编组的每个元素
    '''
    aliens.draw(screen)
    bg_player.drew_myplayer()
    #开始时，不活跃的游戏，创建按钮
    if not stats.game_active:
        button.draw_button()

    #显示得分
    scoreborad.show_score()
    # 刷新屏幕
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,scoreboard,ship,aliens,bullets):
    '''打包子弹的所有操作'''
    #更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 or not stats.game_active :
            bullets.remove(bullet)
    check_bullet_alien_collsions(ai_settings,screen,stats,scoreboard,ship,aliens,bullets)

def fire_bullet(ai_settings,screen,ship,bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,
                        aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.get_rect():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,screen,stats,sb,ship,
                        aliens,bullets)
            break
def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():#利用alien中的返回值True进行判断
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1#通过-1改变移动方向

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb):
    '''
    检查是否有外星人位于屏幕边缘，并更新整群外星人的位置
    '''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb)

def check_bullet_alien_collsions(ai_settings,screen,stats,
        scoreboard,ship,aliens,bullets):
    '''判断子弹是否撞击到外星人，并在消灭所有敌人后重新配置游戏'''
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    #击落飞船，就提高分数
    if collisions:
        scoreboard.prep_ships()
        for aliens in collisions.values():
            stats.scores += ai_settings.alien_points * len(aliens)
            scoreboard.prep_score()
        check_high_score(stats,scoreboard)
    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        scoreboard.prep_level()
        sleep(5)
        create_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets,sb):
    '''响应被外星人撞到的飞船'''
    #将ships_left减1
    if stats.ships_left > 0:
        stats.ships_left -= 1
        #清空外星人列表和子弹列表
        bullets.empty()
        aliens.empty()
        #创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        stats.scores = 0
        sb.prep_ships()

        #暂停
        sleep(1.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(stats,scoreboard):
    if stats.scores > int(stats.high_score):
        scoreboard.prep_high_score()

def check_history_scores(stats):
    file = open('history_scores.txt')
    file.write(stats.high_score)
    file.close()

