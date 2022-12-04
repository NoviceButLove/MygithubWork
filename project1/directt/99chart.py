for i in range(1,10):
    for o in range(1,i+1):#You will find it that if the last number is equivalent to the first ,the computer won't get it to calculate
        print(str(i)+'*'+str(o)+'='+str(i*o),end=' ')
    else:
        print(end='\n')


