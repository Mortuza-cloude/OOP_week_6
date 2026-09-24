class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self. balance = balance

    def deposit(self,amount):
        self.balance += amount

    def show_balance(self):
         print("Current Balance:", self.balance)

accounts =[]

a_number = int(input( "How many  accounts?: "))

for i in range(a_number):
    name = input("Enter account name: ")
    balance = float(input( "Enter initial balance: "))

    account = BankAccount(name, balance)
    accounts.append(account)

for account in accounts:
    account.show_balance()