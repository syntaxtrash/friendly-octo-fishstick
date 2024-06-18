from bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}

    def add_account(self, account_name, int_rate=0.02, balance=0):
        self.accounts[account_name] = BankAccount(int_rate, balance)

    def make_deposit(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].deposit(amount)
        else:
            print(f"Account '{account_name}' does not exist.")

    def make_withdrawal(self, account_name, amount):
        if account_name in self.accounts:
            self.accounts[account_name].withdraw(amount)
        else:
            print(f"Account '{account_name}' does not exist.")

    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            balance = self.accounts[account_name].balance
            print(f"{self.name}'s {account_name} balance: ${balance}")
        else:
            print(f"Account '{account_name}' does not exist.")

    def transfer_money(self, amount, other_user, my_account_name, other_account_name):
        if my_account_name in self.accounts and other_account_name in other_user.accounts:
            if self.accounts[my_account_name].balance >= amount:
                self.accounts[my_account_name].withdraw(amount)
                other_user.accounts[other_account_name].deposit(amount)
                print(f"Transferred ${amount} from {self.name}'s {my_account_name} to {other_user.name}'s {other_account_name}")
            else:
                print("Wala ng pira for transfer.")
        else:
            print("One of the accounts does not exist.")

if __name__ == "__main__":
    user1 = User("Joci", "joci@example.com")
    user1.add_account("checking", int_rate=0.02, balance=500)
    user1.add_account("savings", int_rate=0.03, balance=1000)

    user2 = User("Aaron", "aaron@example.com")
    user2.add_account("checking", int_rate=0.02, balance=300)

    # Deposit, withdrawal, display balance
    user1.make_deposit("checking", 200)
    user1.make_withdrawal("savings", 50)
    user1.display_user_balance("checking")
    user1.display_user_balance("savings")

    # Transfer money
    user1.transfer_money(100, user2, "checking", "checking")
    user1.display_user_balance("checking")
    user2.display_user_balance("checking")

