class BankAccount:
    # MODIFY to initialize a number attribute
    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    # Define __eq__ that returns True if the number attributes are equal
    def __eq__(self, other):
        return self.number == other.number

# Create accounts and compare them
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)
