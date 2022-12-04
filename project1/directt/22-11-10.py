import random
list1=[18,2208,520,521,1111,'hello','world']
list1[1:3]=[]
print(list1)
list1.pop(3)#pop up the element in special index
print(list1)
print(list1.pop())#default cut the last element
'''clear   use to clean up the element in a list'''
print('----------------------------------------------')
print('Next you will see a sequence')
a=list([1,2,3,5,5])
print(a)
print(a.clear())
print(bool(a))
#del    destroy the list totally
del a
#print(a)# NameError: name 'a' is not defined
print('-------------------------------------------')
list1.sort()
print(list1)
c=['hello','world']
'''
list1.extend(c)
list1[2]='hi'
print(list1)
list1[2:6]=[1,2,3]
list1.sort(reverse=True)
print(list1)
list1.sort(reverse=False)
print(list1)

Be careful,when a list contain two or more different tpye data,it can't be sorted properly'''
print('------------------creat a list-------------------------')

'''for ii in range(50):# 用  ii 遍历，做50次循环

    a=random.randint(-200,200)#设置变量a
    list2='None'                                #想建立一个列表（list2=[]
    list2=list()                                #list 用法有误，应是list4=list2.list()
    list2.extend(a)                             #用extend将变量a的值放入列表list2
'''
list2=[11,22,33,44,55,66,77,88,99,12512,252332,235235,45636,54685747,2564643]
'''
for ii in range(5):
    list2.extend(ii)
else:
    print(list2)
'''
list2.sort(reverse=True)#reverse      from high to low
print(list2)
list2.sort(reverse=False)#  from low to high
print('--------------sort---------------------------')
print(list2)
list3=sorted(list2,reverse=True)
print('---------------------creat a list containing a number of numbers----------------------------')
list4=[]
for iio in range(200):
    xxx=random.randint(-100,200)
    list5=[xxx]
    list4.extend(list5)
list4.sort(reverse=True)
print(list4)
list4.sort(reverse=False)
print(list4)
'''
for ioi in range(300):
    xx=random.randint(-198,298)
    list5=[]
    list4.append(xx)
    print(list4)
'''














