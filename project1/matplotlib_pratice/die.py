from random import randint

class Die():
    '''表示一个骰（tou）子的类'''

    def __init__(self,num_facet=6):
        '''骰子默认6面'''
        self.num_facet = num_facet
        self.results = []

    def roll(self,num_roll=1):
        '''返回一个点数,默认摇一次'''
        '''创建一个列表存放所有结果'''
        for ii in range(1,num_roll+1):
            result = randint(1, self.num_facet)  # ctrl+B 查看，是闭区间
            self.results.append(result)
            return result


    def cal_frequency(self):
        self.frequency = []
        self.number = self.num_facet+1
        for num in range(1,self.number):
            frequency = self.results.count(num)
            self.frequency.append(frequency)
        return self.frequency

def cal_x_label(*die):
    '''计算所有骰子点数的和，得出x轴坐标'''

    #变量，用于计算骰子和的范围,存放最后结果
    global num_min
    num_max = 0
    num_min = 0
    x_label = []
    for die1 in die:
        num_max += die1.num_facet
    for die1 in die:
        num_min += 1

    #打开文件进行操作
    file = open('die_x_label.txt','r+')
    # 如果之前使用过，删除文件内容
    if file:
        file.truncate()
    #计算范围，以空格分开
    for num in range(num_min, num_max+1):
        file.write(str(num) + ' ')

        '''
        以r+形式打开文件，指针一点一点随着写入而后退，导致后来readline时，从指针位置开始读，而无法显示内容
        针对这个问题，方法如下：
        1.使用seek将指针回调到开头->seek(0)
        2.关闭文件，再次打开即可
        '''
    file.close()
    #方法二
    with open('die_x_label.txt')as file:
    #再次读取，成功获得txt内容
        file2 = file.readline()
    #将txt中的结果一一写入列表
    for x_label1 in file2.split():
        x_label.append(x_label1)
    #file.close()
    return x_label




if __name__ == '__main__':
    die1 = Die(8)
    die2 = Die(10)
    print(cal_x_label(die1,die2))



