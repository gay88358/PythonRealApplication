class Account:
    def __init__(self, filePath):
        self.filePath = filePath
        with open(self.filePath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount): 
        self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filePath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    def __init__(self, filePath):
        Account.__init__(self, filePath)
        self.fee = 10
    def transfer(self, amount):
        Account.withdraw(self, amount)
        self.balance = self.balance - amount - self.fee

account = Account("./balance.txt")
print("before withdraw: " + str(account.balance))
account.withdraw(100)
print("after withdraw: " + str(account.balance))
account.commit()

ck = Checking("./balance.txt")
print("before transfer: " + str(ck.balance))
ck.transfer(100)
print("after transfer: " + str(ck.balance))
ck.commit()
