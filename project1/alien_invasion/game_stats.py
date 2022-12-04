class GameStats():#类名用大驼峰
    '''跟踪游戏的统计信息'''

    def __init__(self,ai_settings):
        '''初始化统计信息'''
        self.ai_settings = ai_settings
        self.reset_stats()
        #让游戏一开始处于非活动状态
        self.game_active = False
        try:
            with open('history_score.txt') as file:
                if file.read():
                    high_score = file.read()
                else:
                    file.write('0')
        except FileNotFoundError:
            file = open('history_score.txt','w')
            file.write('0')
            file.close()
            high_score = file.read()
        file = open('history_score.txt','r')
        high_score = file.read()
        self.high_score = int(high_score)
        file.close()


    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.game_active = False
        self.ships_left = self.ai_settings.ship_limit
        self.scores = 0
        self.level = 1

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score,-1))


