print(1+2)
print("hello\tworld")
print("helloooo\t\tworld")
print("hello\t\tworld")
print("hello\rworld")       #re..
print("hello\bworld")       #backplace
print("今天开始学习python，我非常高兴，谢谢李师兄！")
print("Teacher say 'I`m your mathematics teacher'")
print('Teacher say \'I`m your mathematics teacher\'')#反斜杠表示转义
print(r"hello\nworld")#The r or R indicate that the function of transfer letter is canceled#
"""Here is the definition of a 
function 
You can learn something from the 
definition"""


'''Next section of lesson'''
n1=33
n2=22.3
n3='Hello'
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))


name='梁锦程'
studentid=20221111145
print(type(name))
print(name)
print(studentid)
'''You can output the outcome only when it is one type'''
#print('My name is'+name+'Here is my ID'+studentid)            #TypeError: can only concatenate str (not "int") to str
'''The main problem is that you couldn`t use the conjunction to connect two different type '''
print('My name is'+str(name)+' Here is my ID '+str(studentid))
'''Now you see ,when use the formulation ;str; every type are transitted into one type
   There may have another solution see as follow:
'''
studentid1='20221111145'
print('My name is '+name+' and my student ID is '+ studentid1)