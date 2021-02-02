class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,value1):
        self.balance = self.balance + value1
        print('Deposit Accepted')

    def withdraw(self,value2):
        if value2 > self.balance:
            print('Funds Unavailable')
        else:
            self.balance = self.balance - value2
            print('Withdrawal Accepted')
    def __str__(self):
        return (f'Account owner: {self.owner} \nAccount balance: {self.balance}')

acct = Account("Ulan",1000)

acct.withdraw(1000)
print(acct)

acct.deposit(850)
print(acct)






