# range()   use to create a int type list of number
print(range(100))
print(type(range(100)))
list1 = range(10)
print(type(list1))
print(list1)
print(list(list1))
print(10 in list1)#range default from 0 to the number you entered
print(11 not in list1)
print(list(range(1,10)))#include the first number but exclude the final number
print(list(range(1,10,2)))#use an parameter to define how the range to walk
print('-------------------------------------------------------------------------')
fir=0
res=0
while fir<=100:
    res+=fir
    fir+=2
print('Outcome :'+str(res))
print('--------------------------------for in -------------------------------------')
for item in range(1,10):
    print(str(item),end=' ')
print('\n')
item1=0
res1=0
for item1 in range(101):
    if item1 % 2 == 0:
        res1+=item1
print('Outcome is:'+str(res1))
print('-----------------------------------------------------------')
for sugar in range(100,1000):
    bai=sugar//100
    shi=(sugar-bai*100)//10
    ge=sugar-bai*100-shi*10
#remember the difference between  //(整除，101//10=10) and %(取余，101%10=1)
    if (bai**3+shi**3+ge**3==sugar):
        print('Congratulation!You have find a sugar baby '+str(sugar))
    else :
        pass
print('------------break and continue-----------------------')
#break will damage the proceeding circle,continue will keep the proceeding circle but jump out of it
for ii in range(5):#Use debug to see how the program is proceeding
    for oo in range(1,11):
        if oo%2==0:
            continue
        else:


            print('This is an odd number: '+str(oo))


    ii+=ii
print('------------------------------------')
lis=[1,2,3,'5','666',2.1,True]
print(lis)
print(lis[2])
print(lis[1:3:])#slice
a=lis[1:3:]#lis[] is use to cut something
print(id(a),id(lis))#You can see the location of the different list is not the same
lis.append(23423)#Only can add one element
print(lis)
lis.extend(a)#The function is plus the a (type:list) after list lis directly
print(lis)
lis[3:]=list1#Use list1 to replace the section cut
print(lis)
#if you want to check  is a special element in the list ,use the    in   or   not in
print(10 in lis)
print(2 not in lis)
#Use  index  to find the index of a element,but be careful it only return the first index it has found
print(lis.index(3))
print(lis.index(3,3,))#From index 3 to the end ,in this range it finds the int 3
print('------------------------')
lis=[1,2,3,'5','666',2.1,True]
lis.extend(list1)
print(lis)
lis.remove(3)
print(lis)# You see it only remove the first element it has found






