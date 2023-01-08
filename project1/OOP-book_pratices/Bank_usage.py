from class_account_newWay import Account


class Bank():
    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 0

    def check_passWord(self, thisPassword, thisAccountNumber):
        thisAccount = self.accountsDict[thisAccountNumber]
        if thisPassword != thisAccount.password:
            print("Incorrect password!")
            return False
        else:
            return True

    def enter_PassWord(self, userAccountNumber):
        num = 0
        lock = False
        while num <= 3 and not lock:
            if num != 3:
                thisPassword = input("Please enter your password:\n")
                token = self.check_passWord(thisPassword=thisPassword, thisAccountNumber=userAccountNumber)
                if token:
                    lock = True
                    return thisPassword
                else:
                    num += 1
                    print('Wrong Password!')
            else:
                print('Your opportunities worn out!')
                return None

    def createAccount(self, theName, theStartingAmount, thePassword):
        oAccount = Account(theName, theStartingAmount, thePassword)
        newAccountNumber = self.nextAccountNumber
        self.accountsDict[newAccountNumber] = oAccount
        self.nextAccountNumber += 1
        return newAccountNumber

    def openAccount(self):
        print('*** Open Account ***')
        userName = input('What is the name for the new user account?')
        userStartingAmount = input('What is the starting balance for this account?')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What is the password you want to use for the account?')

        userAccountNumber = self.createAccount(userName, userStartingAmount, userPassword)
        print('Your new account number is:', userAccountNumber)
        print()

    def closeAccount(self):
        print('*** Close Account ***')
        userAccountNumber = input('What is your account number?')
        userAccountNumber = int(userAccountNumber)
        userPassword = self.enter_PassWord(userAccountNumber)
        if userPassword:
            oAccount = self.accountsDict[userAccountNumber]
            theBalance = oAccount.getBalance(userPassword)
            if theBalance is not None:
                print('You had', theBalance, ' in your account, which is being returned to you.')
                del self.accountsDict[userAccountNumber]
                print('Your account is now closed.')

    def balance(self):
        print('*** Get Balance ***')
        userAccountNumber = input('What is your account number?')
        userAccountNumber = int(userAccountNumber)
        userPassword = self.enter_PassWord(userAccountNumber)
        if userPassword:
            oAccount = self.accountsDict[userAccountNumber]
            theBalance = oAccount.getBalance(userPassword)
            if theBalance is not None:
                print('Your balance is:', theBalance)

    def deposit(self):
        print('*** Deposit ***')
        accountNum = input('Please enter the account number: ')
        accountNum = int(accountNum)
        depositAmount = input('Please enter amount to deposit: ')
        depositAmount = int(depositAmount)
        thisPassword = self.enter_PassWord(accountNum)
        if thisPassword:
            oAccount = self.accountsDict[accountNum]
            theBalance = oAccount.deposit(depositAmount, thisPassword)
            if theBalance is not None:
                print('Your new balance is:', theBalance)

    def show(self):
        print('*** Show ***')
        for userAccountNumber in self.accountsDict:
            oAccount = self.accountsDict[userAccountNumber]
            print('\t\tAccount:', userAccountNumber)
            oAccount.show()

    def withdraw(self):
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number:')
        userAccountNumber = int(userAccountNumber)
        userAmount = input('Please enter the amount to withdraw: ')
        userAmount = int(userAmount)
        userAccountPassword = input('Please enter the password: ')
        oAccount = self.accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userAmount, userAccountPassword)
        if theBalance is not None:
            print('Withdrew:', userAmount)
            print('Your new balance is :', theBalance)

# show() & withdraw()
