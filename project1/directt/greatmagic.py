global namelist
namelist = []
def magician_name(name = 'Alan Tulin'):

    kaiguan = True
    while kaiguan:
        nam = input('Please enter a magician`s name  ')
        namelist.append(nam)
        jud = input('Enter yes/ no to continue or leave ')
        if jud == 'no':
            kaiguan = False

def shownam():
    for nam1 in namelist:
        nam1 = str(nam1)
        print('The great magician is '+nam1.title())

magician_name()
shownam()