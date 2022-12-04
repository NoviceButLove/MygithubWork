class Dog:
    def __init__(self,name,age,size):
        print('狗子初始化成功')
        self.name = name
        self.age = age
        self.size = size
    def response(self):
        ask = input('Enter yes/no to decide if call the dog ')
        if ask == 'yes':
            print('Dog said his name is '+ self.name)
        else :
            print('Cure dog, I love you')
    def jump(self):
        print('Dog '+self.name+' jump up')
        print('He is '+str(self.age) +' years old '+'Size '+str(self.size))
dog1 = Dog('XIAOHUANG',12,12)
dog1.response()
dog1.jump()

