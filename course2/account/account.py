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

account = Account("./balance.txt")
print("before withdraw: " + str(account.balance))
account.withdraw(100)
print("after withdraw: " + str(account.balance))
account.commit()