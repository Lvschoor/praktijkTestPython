class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


account = BankAccount("Alex")
print('Name of the account holder:', account.owner)
print('Starting balance of the account:', account.balance)
print('Balance after a deposit:', account.deposit(10))
print('Balance after a withdrawal:', account.withdraw(3))

