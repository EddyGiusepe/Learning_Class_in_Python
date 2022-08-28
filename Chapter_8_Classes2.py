'''
Data Scientist.: Dr.Eddy Giusepe Chirinos Isidro
'''
# Markdown --> https://raullesteves.medium.com/github-como-fazer-um-readme-md-bonit%C3%A3o-c85c8f154f8

class BankAccount:
    def __init__(self, first_name, last_name, number, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def print_info(self):
        first = self.first_name 
        last = self.last_name
        number = self.number 
        balance = self.balance

        s = f'{first} {last}, {number}, balance: {balance}'
        print(s)


a1 = BankAccount('John', 'Olsson', '19371554951', 20000)
a1.deposit(1000)
a1.print_info()

