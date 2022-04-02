import random, sys, os

class Account:
    def __init__(self,account_number,customer_name,pin,balance = 0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.pin = pin
        self.balance = balance
    
    def __repr__(self):
        return f'Account("{self.account_number}","{self.customer_name}",{self.pin},{self.balance})'

    def pin_verification(self,pin):
        if self.pin == pin:
            return True
        else:
            return False

    def check_balance(self):
        print(f"Your current balance is £ {self.balance}")

    def deposit(self,ammount):
        self.balance += ammount
        print(f"£{ammount} has been added to your account")

    def withdraw(self,ammount):
        if ammount > self.balance:
            print(f"Insufficient Funds, your balance is currently £{self.balance}") 
        else:
            self.balance -= ammount
            print(f"£{ammount} has been withdrawn from your account")

        
#Account Creation
accounts = []
#account number generator
def account_number_gen():
    random_nums = []
    for i in range(10):
        n = random.randint(0,9)
        random_nums.append(n)
        account_num = int("".join(map(str,random_nums)))
    return account_num
account_number = account_number_gen()

#PIN Generator 
def pin_number_gen():
    random_nums = []
    for i in range(4):
        n = random.randint(0,9)
        random_nums.append(n)
        pin_num = int("".join(map(str,random_nums)))
    return pin_num
pin = pin_number_gen()

def get_customer_name():
    name = input("Please enter your name: ")
    return name
customer_name = get_customer_name()

account = Account(account_number,customer_name,pin,0)
accounts.append(account)
print(f"Hello {customer_name}")
print(f"Your account number is: {account_number}")
print(f"Your new PIN is {pin}")
input(f"Pres enter to continue: ")

os.system('cls' if os.name == 'nt' else 'clear')

#ATM interface
def main():
    while True:
        print(f"Welcome to the Bank of Python.")
        pin = int(input(f"Please enter your PIN: "))
        while account.pin_verification(pin) != True:
            pin =int(input(f"Incorrect PIN please try again: "))
            
        while True:
            print(f"Welcome {customer_name}, Account Number: {account_number} what would you like to do today?")
            print("1: Check Balance")
            print("2: Deposit Cash")
            print("3: Withdaw Cash")
            print("4: Exit")
            
            user_choice = int(input(f"Please enter a numerical selection: "))

            if user_choice == 1:
                account.check_balance()
               
            elif user_choice == 2:
                ammount = float(input("Please enter ammount you wish to deposit:"))
                account.deposit(ammount)
                
            elif user_choice == 3:
                ammount = float(input("Please enter ammount you wish to withdraw:"))
                account.withdraw(ammount)
                
            elif user_choice == 4:
                print("Thanks for choosing the Bank of Python")
                exit()

            else:
                print("Invalid Choice! Please select from 1,2,3,4 ")

main()
