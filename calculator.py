class MyCalc:
    def __init__(self, fname, lname, balance=0):
        self.firstname = fname
        self.lastname = lname
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposit: +{amount}')
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdrawal: -{amount}')
            return self.balance
        else:
            return 'Sorry, you do not have sufficient funds to complete this operation'

    def calculate_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        self.transaction_history.append(f'Interest added: +{interest}')
        return interest

    def account_info(self):
        return f"Account Information: \nName: {self.firstname} {self.lastname}\nBalance: {self.balance}"

# Example usage:
demo_account = MyCalc('OJUKA', 'CLIFFORD', 1000)
print('Initial Account Info:')
print(demo_account.account_info())

demo_account.deposit(500)
print('\nAfter deposit of 500:')
print(demo_account.account_info())

demo_account.withdraw(200)
print('\nAfter withdrawal of 200:')
print(demo_account.account_info())

demo_account.calculate_interest(2.5)
print('\nAfter adding interest of 2.5%:')
print(demo_account.account_info())

print('\nTransaction History:')
for transaction in demo_account.transaction_history:
    print(transaction)
