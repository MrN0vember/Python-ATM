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

    def login():
        attempts = 0
        while attempts < 4:
            pin = input("Please enter your 4 digit PIN: ")
            if pin_verification(pin):
                print("PIN Accepeted")
                return True
            else:
                print("Inccorect PIN")
                attempts += 1
        print("Too many inccorect. Please contact your bank")
        return False

        
            


    