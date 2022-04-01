class BankAccount:
    def __init__(self,account_number,customer_name,pin,balance = 0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.pin = pin
        self.balance = balance

    def pin_verification(pin):
        if self.pin == pin:
            retrun True
        else:
            return False
            
    