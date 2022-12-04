def judge(num):
    for ii in range(0,num):
        num1=int(input('Please a number,let me judge if it is a odd or doub: '))
        odd=[]
        doub=[]
        '''
                if num1==1:
            odd.append(num1)
        elif num1%2!=0:
            odd.append(num1)
        else:
            doub.append(num1)
        '''
        if num1%2:
            odd.append(num1)
        else:
            doub.append(num1)
    print('Odd Number: ')
    print('Doub number:')
    print(odd)
    print(doub)

#   print('Please enter the amount you want to play the Game__--Judge')
num=int(input('Please enter the amount you want to play the Game__--Judge: '))
judge(num)
