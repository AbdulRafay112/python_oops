# R-2.5 Use the techniques of Section 1.7 to revise the charge and make payment
# methods of the CreditCard class to ensure that the caller sends a number
# as a parameter

class CreditCard:
    """A Consumer Credit Card"""
    def __init__(self , customer , bank , acnt , limit):
        """Create a new credit card instance
        The initial balance is zero 
        Args:
             customer: the name of the customer 
             bank : the name of the bank
             acnt: the account identifier 
             limit: credit card limit
        """
        self._customer = customer 
        self._bank = bank 
        self._acnt = acnt 
        self._limit = limit 
        self._balance = 0 
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
