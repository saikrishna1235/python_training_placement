class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
    def deposit(self,amount):
        self.__balance += amount
        print("amount deposited")
    def get_balance(self):
        print("Current balance :",self.__balance)

Account = BankAccount(500)
Account.deposit(5000)
Account.get_balance()
