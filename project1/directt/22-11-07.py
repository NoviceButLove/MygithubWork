a=100
b=20.0
print(type(a))
print(type(b))
a*=10
print(a)
a/=3
print(a,type(a))
#how to transfer the cursor to the end of a line!!!!
a//=3
print(a,type(a))
a%=2
print(a,type(a))
a,b,c=10,20,30    #unpack and evulation. This function can exchange two variable quantity's number
print(a,b,c,a+b+c)
a,b,c=c,a,b
print(a,b,c)
print('whether a>b?',a>b)#In print ,contrast will be outputed by bool
print(a!=b)#is a inequivalent to b
print(a==b)#is a equivalent to b        In here ,they just compare the value
'''
Next , we will learn that the function  'is' and 'is not'

'''

#first creat two pile numbers
list1=[1,2,3,5]
list2=[1,2,3,5]
print("==比较的是数组里的值，is 询问的是id是否相等，is not 反之")
print(list1==list2)
print(list1 is list2)#the result's type is bool
print(list1 is not list2)
print(str(id(list1))+'\n'+str(id(list2)),end='\n')
'''
print(id(list1),'\n',id(list2))
use this to see the contrast,you have learned the usage of \n
'''
#bool
a,b=10,20
print(a==10 and b==20)#and 和运算    or 或运算    not    否运算
print(a!=10 and b==20)

print(a!=10 or b==20)
bb = True
print(not bb)
#in          not in       use to check if the special string have the string you wanted
me='helloworld,ok'
print(',' in me)
print(not 'h' not in me)#double negative judge,hope you don't get it false
print(str(id(list1))+'\n'+str(id(list2)))
print(type(id(list1)))

















