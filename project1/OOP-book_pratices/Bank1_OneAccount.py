# non-OOP version

accountList = [{'name': 'Joe',
                'balance': 1100,
                'password': 'soup',
                'token': True},
               {'name': 'Mike',
                'balance': 3200,
                'password': 'rabbit',
                'token': True}]


def enter_passWord(accountNumber):
    thisAccountDict = accountList[accountNumber]
    num = 0
    thisPassword = input("Please enter the password:\n")
    while num <= 3:
        if num != 3:
            if thisPassword != thisAccountDict['password']:
                print("Incorrect password!")
                num += 1
                print("Please enter again!:\n")
            else:
                return True
        else:
            print('Your opportunities worn out!')
            return False


def newAccount(aName, aBalance, aPassword):
    global accountList
    newAccountDict = {'name': aName, 'balance': aBalance, 'password': aPassword, 'token': True}
    accountList.append(newAccountDict)


def show(accountNumber):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if thisAccountDict['token']:
        print('Account', accountNumber)
        thisAccountDict = accountList[accountNumber]
        print('\t\tName', thisAccountDict['name'])
        print('\t\tBalance:', thisAccountDict['balance'])
        print('\t\tPassword:', thisAccountDict['password'])
        print()
    else:
        print("Your token is frozen")
        thisAccountDict['token'] = False

def getBalance(accountNumber):
    global accountList
    thisAccountDict = accountList[accountNumber]
    token = enter_passWord(accountNumber)
    if token:
        print("Your balance is: ", thisAccountDict['balance'])
    else:
        thisAccountDict['token'] = False
        print("Your token is frozen")


def deposit(accountNumber):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if thisAccountDict['token']:
        token = enter_passWord()
        if token:
            amountToDeposit = input("enter the amount to deposit:\n")
            if amountToDeposit < 0:
                print("You cannot deposit a negative amount!")
                return None
            else:
                thisAccountDict['balance'] += amountToDeposit
        else:
            thisAccountDict['token'] = False
            print("Your token is frozen")


def withdraw(accountNumber):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if thisAccountDict['token']:
        token = enter_passWord(accountNumber)
        if token:
            amountToWithdraw = input("enter the amount to deposit:\n")
            if amountToWithdraw < 0:
                print("You cannot deposit a negative amount!")
                return None
            elif amountToWithdraw > thisAccountDict['balance']:
                print("Sorry, you have enough money to withdraw")
            else:
                thisAccountDict['balance'] -= amountToWithdraw
        else:
            thisAccountDict['token'] = False
            print("Your token is frozen")


def check_keyDown_event():
    accountNumber = input("Please enter you account number:\n")
    if accountNumber < 0 | accountNumber >= len(accountList):
        print("Wrong account number!!")
    else:
        action = input('What do you want to do?\n')
        if action == 'b':
            getBalance(accountNumber)
        elif action == 'd':
            deposit(accountNumber)
        elif action == 's':
            show(accountNumber)
        elif action == 'w':
            withdraw(accountNumber)
        elif action == 'n':
            aName = input("Please enter your name: ")
            aBalance = input("Please enter the initialize money your want to store in bank: ")
            aPassword = input("Please enter the password: ")  # 之后可设置输两次验证
            newAccount(aName, aBalance, aPassword)


while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print("Press n to create a new account")
    print()

    check_keyDown_event()
    lastAction = input('Is there anything else?(enter q to quit)')
    if lastAction == 'q':
        print("Done!")
        break
