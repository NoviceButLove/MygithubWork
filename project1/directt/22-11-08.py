enligsh='my nAMe is xxx,i nEEd a friend to company with me'
print(enligsh.title())
print(enligsh.upper())
print(enligsh.lower())
first_name='Alan'
given_name='Walk'
print(first_name+'\n'+given_name)#You can use '+'to connect two string type variable quantity
context='language is different'
print(context.rstrip())
something_bad='what the fuck here have some shit'
print(something_bad.lstrip('wh'))#delete until the special string could't be find
# import this    -------this is an important indispensable tips for the novice,I  hope some day you will use it to improve youself come on friend!
#Next we will learn the function  a powerful function  ---- list----
#Created through []
name_list=['liang','liu','zhang','zhou']
print(name_list[2].title())
'''
Be careful the id of the first element of a list is 0 not the 1
'''
#Another ,you can use -1 to indicate the last element
print(name_list[-1].title())#extract the last element
#You can always revise the element of a list
#As you know ,appendix is a elementary organ in our body
name_list.append('Aoligei')
print(name_list[-1].lower)
name_list.append('Aoligei')
print(name_list)
'''
In this way ,you see that altough the two element is same ,their id may different .
So the second element still will be added into the name_list
embraassed the reason I supposed is wrong false
'''
print(id(name_list[-1]),id(name_list[-2]))
name_list.insert(1,'aoligeidashu')
print(name_list)
#On the contrary we could use del to delete a element from a list
del name_list[2]
print(name_list)
#use .pop() to get a element out of list
pop_name_list=name_list.pop()
print(pop_name_list)#You can use the extraction
print(name_list)#The last element have been deleted
'''
If you don't know the exactly location of a element .
Whereas you still won't to get it out of the list
try to use  function   'remove'
'''
not_wanted='liang'
name_list.remove(not_wanted)
print(name_list)#Be careful Watching!!!the element must be in the list
#You should check the name of the element .Remenber if you have written it in capital
#sort() sort out the element in the list.It is irreversible
#sorted() the function is same as sort() but is reversible
print('------------------next is the pratise of sort() and sorted()-------------------')
a=sorted(name_list)
print(name_list)
name_list.sort()
print(name_list)
#See the different usage of the function .sort()  sorted()
print('--------------------------------------------------------------')
print(4|8)
print(4&8)
print(4>>1)
print(4<<1)