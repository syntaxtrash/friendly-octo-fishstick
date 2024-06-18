class BankAccount:
    accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate=0.01, balance=0):
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.interest_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Wala na pira: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.accounts:
            print(f"Balance: {account.balance}")

if __name__ == "__main__":
    # Create 2 accounts
    account1 = BankAccount()
    account2 = BankAccount(0.02, 1000)

    """
    To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in 
    one line of code
    """
    account1.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()

    """
    To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code
    """
    account2.deposit(200).deposit(300).withdraw(100).withdraw(50).withdraw(20).withdraw(10).yield_interest().display_account_info()

    # Print all accounts info 
    BankAccount.print_all_accounts_info()
