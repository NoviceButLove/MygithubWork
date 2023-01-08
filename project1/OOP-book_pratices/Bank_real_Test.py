# 主程序

# 导入所有相关的文件
from Bank_usage import *
oBank = Bank()
joesAccountNumber = oBank.createAccount('Joe', 1000, 'soup')
print("Joe's account number is :", joesAccountNumber)


def check_keyDown_event():
    accountNumber = int(input("Please enter you account number:\n"))
    if accountNumber < 0 | accountNumber >= oBank.nextAccountNumber:
        print("Wrong account number!!")
    else:
        action = input('What do you want to do?\n')
        if action == 'b':
            oBank.balance()
        elif action == 'd':
            oBank.deposit()
        elif action == 'c':
            oBank.closeAccount()
        elif action == 's':
            oBank.show()
        elif action == 'w':
            oBank.withdraw()
        elif action == 'o':
            aName = input("Please enter your name: ")
            aBalance = input("Please enter the amount of money to initialize  your want to store in bank: ")
            aPassword = input("Please enter the password: ")  # 之后可设置输两次验证
            oBank.createAccount(aName, aBalance, aPassword)
        else:
            print('Sorry!')


while True:
    print()
    print('Press b to get the balance')
    print('To close an account, press c')
    print('To open a new account, press o')
    print('Press d to make a deposit')
    print('Press w to make withdrawal')
    print('Press s to show all the account')
    print('Press q to quit')
    print("Press n to create a new account")
    print()

    check_keyDown_event()
    lastAction = input('Is there anything else?(enter q to quit)')
    if lastAction == 'q':
        print("Done!")
        break
