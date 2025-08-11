class CreditCard:
    """A Consumer Credit Card"""
    def __init__(self , customer , bank , acnt , limit , initial_balance = 0):
        """Create a new credit card instance
        The initial balance is zero 
        Args:
             customer: the name of the customer 
             bank : the name of the bank
             acnt: the account identifier 
             limit: credit card limit
        """
        if not isinstance(initial_balance , (int , float)):
            raise TypeError("balance should be a number")
        if initial_balance < 0:
            raise ValueError("balance should be positive or zero")
        self._customer = customer 
        self._bank = bank 
        self._acnt = acnt 
        self._limit = limit 
        self._balance = initial_balance
    def get_customer(self):
        """get customer name"""
        return self._customer
    def get_bank(self):
        """get bank of customer""" 
        return self._bank 
    def get_acnt(self):
        """Get acnt of the customer"""
        return self._acnt 
    def get_limit(self):
        """Get limit amount of credit card """
        return self._limit
    def get_balance(self):
        """get balance of the customer"""
        return self._balance
    def charge(self , amount):
        """Charge given price to the card assuming sufficient credit card limit
        return True if charge was proceed other wise return false
        """
        if self._balance + amount > self._limit:
            return False 
        if not isinstance(amount , (int , float)):
            raise ValueError("amount must be a number")
        else:
            self._balance += amount 
            return True 
    def make_payment(self , amount):
        """process customer payment that reduces balance"""
        if not isinstance(amount , (int , float)):
            raise ValueError("amount must be a number")

        self._balance -= amount 

wallet: list[CreditCard] = []
wallet.append(CreditCard("Rafay" , "HBL" , 1234 , 1000))
wallet.append(CreditCard("Moiz" , "Meezan" , 1234 , 12000 , 500))
wallet.append(CreditCard("Bilaal" , "UbL" , 1234 , 800 , 100))

for val in range(1,100):
    wallet[0].charge(val/10)
    wallet[1].charge(val/2)
    wallet[2].charge(3*val)
for c in range(3):
    print(f"{wallet[c].get_customer()} has {wallet[c].get_balance()}(limit = {wallet[c].get_limit()})")

