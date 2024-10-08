# Class to represent a BankAccount
class BankAccount:
    # __init__ method to initialize the account with a starting balance
    def __init__(self, starting_balance):
        self.__balance = starting_balance  # private attribute

    # Method to add an amount to the balance
    def deposit(self, amount):
        self.__balance += amount

    # Method to subtract an amount from the balance if sufficient funds are available
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount

    # Method to return the current balance
    def get_balance(self):
        return self.__balance


# Sample Input
account = BankAccount(1000)

# Deposit money and check balance
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Withdraw money and check balance
account.withdraw(300)
print(account.get_balance())  # Output: 1200

# Attempt to withdraw more than available balance
account.withdraw(1500)  # Output: Insufficient funds!
