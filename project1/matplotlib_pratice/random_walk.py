from random import choice

class Randomwalk():
    '''一个生成随机漫步数据的类'''

    def __init__(self,num_points= 5000):
        '''初始化'''
        self.num_points = num_points

        #随机漫步始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''计算随机漫步包含的所有点'''

        #不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            self.x_step = self.get_step()
            self.y_step = self.get_step()

            #拒绝原地踏步
            if self.x_step == 0 and self.y_step == 0:
                continue

            #计算下一个点的x和y值
            next_x = self.x_values[-1] + self.x_step
            next_y = self.y_values[-1] + self.y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        self.direction = choice([1,-1])
        self.distance = choice([0,1,2,4,8,16,32,64,128,256])
        self.step = self.distance * self.direction
        return self.step
