# 使用class处理函数
# 新增error处理，raise

class AbortTransaction(Exception):  # 继承了Exception类
    """raise this exception to abort a bank transaction"""
    pass


class Account():  # 类没有参数时可删去括号
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def validateAmount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be an integer')
        if amount <= 0:
            raise AbortTransaction('Amount must be positive')
        return amount

    def deposit(self, amountToDeposit, password):
        amountToDeposit = self.validateAmount(amountToDeposit)
        if password != self.password:
            print("Sorry, incorrect password")
            return None
        if amountToDeposit < 0:
            print("You cannot deposit a negative amount of money")
            return None
        self.balance += amountToDeposit
        return self.balance

    def withdraw(self, amountToWithdraw, password):
        amountToWithdraw = self.validateAmount(amountToWithdraw)
        if password != self.password:
            print("Incorrect password for this account")
            return None
        if amountToWithdraw < 0 | amountToWithdraw > self.balance:
            self.balance -= amountToWithdraw
            return self.balance

    def getBalance(self, password):
        if password != self.password:
            print("Incorrect password for this account")
            return None
        return self.balance

    def show(self):
        print("\t\tName:", self.name)
        print("\t\tBalance:", self.balance)
        print("\t\tPassword:", self.password)
        print()
