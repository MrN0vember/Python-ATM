import random

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

    def account_details(self):
        print(f'Account Number: {self.account_number}')
        print(f'Account Holder: {self.customer_name}')

    def check_balance(self):
        return f"Your current balance is £ {self.balance}"

    def deposit(self,ammount):
        self.balance += ammount
        return f"£{ammount} has been added to your account"

    def withdraw(self,ammount):
        if ammount > self.balance:
            return f"Insufficient Funds, your balance is currently £{self.balance}" 
        else:
            self.balance -= ammount
            return f"£{ammount} has been withdrawn from your account"

        
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
    


















    
    





        
            

            


    