import random
step=1
rand=random.randint(-100,200)
num1=input('Please enter a number,it is larger than -100 and smaller than 200\n')
tip='Now you enter a number,see how many steps you need to find the proper number createed by computer'
print(tip.title()+'\n')
num=int(num1)
if num>=-100 and num<=200:
    while(num!=rand):
        step+=1
        if num<rand:
            print('SMALLER')
        else:
            print('LARGER')
        num = int(input('Please enter a number,it is larger than -100 and smaller than 200\n'))
    print('You have use '+str(step)+' steps')
    print('The anwser is '+str(rand))
elif num<-100 or num>200:
    num = int(input('You enter a wrong number\n'))
else:
    print('Maybe you get something wrong '+type(num))
