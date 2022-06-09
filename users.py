class User:
    bank_name = "Bank of the Weast"
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount

Hilde = User("Hilde", "hild@antisocial.com")
Gaston = User("Gaston", "noonefightslikegaston@neckbelts.com")

Hilde.make_deposit(5000).make_deposit(200)
Gaston.make_deposit(12)