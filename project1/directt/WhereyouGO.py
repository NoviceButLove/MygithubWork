keep = True
mes = {}
while keep:
    name = input('Please enter your name: ')
    place = input('Where would you like to go when you free?Pleas enter the place: ')
    mes[name] = place
    kep = input('Do you want to tell us anymore message about what you want to go?(yes/no)')
    if kep == 'no':
        keep = False
for na,pl in mes.items():
    print('Now '+na+' want to go to '+pl+' to enjoy vacation')
