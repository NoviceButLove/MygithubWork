def add1(a,b):
    c = a + b
    return c
while True:
    try :
        a = input('Please enter a number: ')
        b = input('Please enter another number: ')
        print(add1(int(a),int(b)))
    except ValueError:
        print('Please enter a number ,not a string ')
        a = input('Please enter a number: ')
        b = input('Please enter another number: ')
        print(add1(a,b))
    else:
        print('do the right thing, get the right result')
        quit1 = input('Enter q to quit----')
        if quit1 == 'q':
            break