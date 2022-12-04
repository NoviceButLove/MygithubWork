class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name =restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print('Restaurant\'s name is '+self.name)
        print('Their cuisine type is '+self.type)
    def open_restautant(self):
        print('The restautant,'+self.name+' is working')
    def pep_eaten(self,pepnum):
        while True:
            self.number_served = pepnum
            if pepnum <= 0:
                print('\nYou have entered a error number!!!')
                pepnum1 =int(input('Please enter again '))
                self.pep_eaten(pepnum1)
            else:
                print('There are '+str(self.number_served)+' people have eaten in it')
            break
    def increment_number_served(self,ext_num):
        self.ext_num = ext_num
        now1 = self.number_served + self.ext_num
        print('Now there are '+
            str(now1)+' eating in it')

if __name__ == '__main__':#用于处理像这样在设计模块时产生的测试程序

    res1 = Restaurant('ZHONGSHI3','ZIZHU')
    res1.describe_restaurant()
    res1.open_restautant()
    print('-----------------------------------------------')
    res2 = Restaurant('DongBeiJiaoZi','Dumpling',)
    res2.describe_restaurant()
    res2.open_restautant()
    res2.pep_eaten(10)
    res2.increment_number_served(20)

