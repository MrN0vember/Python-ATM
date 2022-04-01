class BankAccount:
    def __init__(self,account_number,customer_name,pin,balance = 0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.pin = pin
        self.balance = balance

    def pin_verification(self,pin):
        if self.pin == pin:
            return True
        else:
            return False

    def account_details(self):
        print(f'Account Number: {self.account_number}')
        print(f'Account Holder: {self.customer_name}')

    def check_balance(self):
        return self.balance

    def deposit(self,ammount):
        self.balance += ammount

    def withdraw(self,ammount):
            self.balance += ammount

    
#Account Creation

Accounts = {}

def account_number_gen()



        
            

            


    