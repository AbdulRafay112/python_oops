# R-2.6 If the parameter to the make payment method of the CreditCard class
# were a negative number, that would have the effect of raising the balance
# on the account. Revise the implementation so that it raises a ValueError if
# a negative value is sent.

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
            raise TypeError("amount must be a number")
        else:
            self._balance += amount 
            return True 
    def make_payment(self , amount):
        """process customer payment that reduces balance"""
        if not isinstance(amount , (int , float)):
            raise TypeError("amount must be a number")
        elif amount < 0 :
            raise ValueError("amount must be a positive")

        self._balance -= amount 
