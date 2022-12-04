def info_rece(manufacturer,edition,*info_causal,**info_other):
    dic_car = {}
    dic_car[manufacturer] = edition
    for x,y in dic_car.items():
        print('The manufacturer is: '+str(x) )
        print('The car`s model is: '+str(y))
    for z in info_causal:
        print(z)
    for a,b in info_other.items():
       # k = info_other.items()
        print('There are some information about the car,like: ',end='')
        print('the '+str(a)+' is '+str(b))

info_rece('Dazhong','AE86',color = 'yellow',size = 'big',appendments = 'rocket')
print('--------------------------------------------------------')
while True:
    mannu = input('Please enter the manufacturer of your car: ')
    model = input('Please enter the model of your car: ')
    oth = input('Please enter something appendment to describe your car: ')
    info_rece(mannu,model,oth)
    kep = input('Enter yes/no to continue ')
    if kep == 'no':
        break

