# R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new account to zero. Modify that class so that a new account can be given a
# nonzero balance using an optional fifth parameter to the constructor. The
# four-parameter constructor syntax should continue to produce an account
# with zero balance.

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