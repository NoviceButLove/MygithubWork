#Yesterday we have learned how to use the str() function
#Now as follows ,we will continue to explore the function int() and float()
'''
In the front of a programme,use "  #coding:   "  and put the type of what you want after the :
this explanation can be treated as a special programme
like this             #coding:utf-8
'''

# first         input()
'''
this programme allow user put sth into the computer to calculate
the thing our put into only could be stored in type of string
'''
gift=input("What do you want, my friend?")
print(gift,type(gift))

a=10
b='hello'
#print(a+b)# the punctuation of + only use to connect two same type thing
#print(int(a)+int(b))#here the function of 'int' could only transform the number strings
c=input('Please enter a number')
d=input('Please enter another number')
'''
In here ,if you don't use the 'int()',the two number only will be connected simply
Because the function of the punctuation , '+',just like this 
'''
print(int(c)+int(d))



'''
Next we will learn the different operator  .For example ,+ -  *  / ,%(取余,**（幂,//（取整
'''
print(11/5)
print(11//5)
print(11%5)
print(11*5)
print(2**10)

a1=12
b1=a1
print(id(b1),id(a1))





