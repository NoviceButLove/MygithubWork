class Settings():
    '''存储游戏相关设置'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #飞船设置
        self.ship_limit = 3

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 2

        #外星人设置
        self.fleet_drop_speed = 10

        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

        self.score_scale = 1.5
        self.speedup_scale = 1.05
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化，动态设置'''
        self.ship_speed_factor = 1.2
        self.bullet_speed_factor = 3
        self.bullets_allowed = 3
        self.alien_speed_factor = 0.4

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        '''提高速度设置,提高配置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.ship_limit += 1
        self.bullets_allowed += 0.5
        self.alien_points = int(self.alien_points * self.score_scale)
