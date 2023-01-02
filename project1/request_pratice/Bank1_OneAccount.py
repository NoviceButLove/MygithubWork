# non-OOP version


message = {'accountName': 'Joe',
           'accountBalance': 100,
           'accountPassword': 'soup',
           'accountToken': True}


def check_keyDown_event(messages):
    action = input('What do you want to do?\n')
    if action == 'b':
        print('Get Balance:')
        token = enter_passWord(messages)
        if token:
            print("Your balance is: ", messages['accountBalance'])
        else:
            messages['accounttoken'] = False
            print("Your token is frozen")
    elif action == 'd':
        print("Deposit: ")
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        token = enter_passWord(messages)
        if token:
            if userDepositAmount < 0:
                print('You cannot deposit a negative amount!')
            else:
                messages['accountBalance'] += userDepositAmount
                print('Your new balance is: ' + messages['accountBalance'])
        else:
            messages['accounttoken'] = False
            print("Your token is frozen")
    elif action == 's':
        print('Show: ')
        print('\t\tName', messages['accountName'])
        print('\t\tBalance:', messages['accountBalance'])
        print('\t\tPassword:', messages['accountPassword'])
        print()
    elif action == 'w':
        print('Withdraw: ')
        token = enter_passWord(messages)
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)

        if token:
            if userWithdrawAmount < 0:
                print('You cannot withdraw a negative amount')
            elif userWithdrawAmount > messages['accountBalance']:
                print('You cannot withdraw more than you have in your account')
                print('Your balance is: ' + messages['accountBalance'])
            else:
                messages['accountBalance'] -= userWithdrawAmount
                print('Your new balance is: ', messages['accountBalance'])


def enter_passWord(messages):
    num = 0
    userPassword = input("Please enter the password:\n")
    while num <= 3:
        if num != 3:
            if userPassword != messages['accountPassword']:
                print("Incorrect password!")
                num += 1
                print("Please enter again!:\n")
            else:
                return True
        else:
            print('Your opportunities worn out!')
            return False


while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    check_keyDown_event(message)
    lastAction = input('Is there anything else?(enter q to quit)')
    if lastAction == 'q':
        print("Done!")
        break
