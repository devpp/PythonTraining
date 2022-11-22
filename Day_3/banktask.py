# Clear screen
import os

os.system('cls')


class Bank_Account:
    def __init__(self):
        self.balance = 0

    #        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def transfer(self):
        amount = float(input("Enter amount to be transferred: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You transferred:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", self.balance)

    # Driver code


# creating an object of class
s = Bank_Account()

# Calling functions with that class object
inp = input(print("""Hello!!! Welcome to the Deposit & Withdrawal Machine \n
1 - deposit \n
2 - withdraw \n
3 - transfer \n
4 - display balance \n
5 - exit \n
:- """))

while inp != 5:
    if inp == "1":
        s.deposit()
    elif inp == "2":
        s.withdraw()
    elif inp == "3":
        s.transfer()
    elif inp == "4":
        s.display()
    elif inp == "5":
        exit()
