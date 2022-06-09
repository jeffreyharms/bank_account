class bank_account:
    list_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        bank_account.list_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display_account_info(self):
        print("Balance: ", self.balance)
    def yield_interest(self):
        self.balance += self.balance*self.int_rate

account_1 = bank_account(0.03, 5000)
account_2 = bank_account(0.05, 20)

account_1.deposit(250).deposit(500).deposit(750).withdraw(1000).display_account_info()
account_2.deposit(400).deposit(350).withdraw(25).withdraw(290).withdraw(50).withdraw(200).yield_interest().display_account_info()