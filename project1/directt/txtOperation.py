from Classtest import Dog
'''
In here you should import the class Dog like this so that you can use the class Dog defined by others
'''
#import Classtest
file1 = open('a.txt','r+')
file1.write('hello world')
print(file1.readline(5))#read until  the index 5,but it begin from 1
file1.flush()
dog1 = Dog('DaHuang',12,14)
dog1.response()
dog1.jump()
file1.close()
