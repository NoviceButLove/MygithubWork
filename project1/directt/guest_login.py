while True:
    print('Welcome to my web ,if you want to play ,please sign in firstly')
    user_name = input('Please enter your user name: \t'+'or ENTER q to quit \n')
    if user_name == 'q':
        break
    user_list = []
    user_list = user_name
    print('Thank for using it!!!')
    with open('guest.txt','a') as file1:
        file1.write(user_name+'\n')
    conti = input('If there somebody else want to sign in ,please enter yes/no ')
    if conti == 'no':
        break
with open('guest.txt')as file1:
    for pop in file1:
        print(pop.rstrip())
print('--------------------------------------')
with open('guest.txt')as fiel1:
    cont = fiel1.read()
    cont = cont.split()
    print(cont)
    print(len(cont))

