


class Account:
    def __init__(self, balance):
        self._balance = balance
    
    def deposit(self, money):
        self._balance = self._balance + money
    
    def withdraw(self, money):
        self._balance = self._balance - money
    
    def balance(self):
        return self._balance



if __name__ == '__main__':
    account = Account(1000)
    print(account.balance())
    