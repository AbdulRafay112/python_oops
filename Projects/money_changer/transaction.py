class Transaction: 
    """This class will take charged and given amount and return the difference between them"""
    def __init__(self , charged_amount , given_amount):
        self._validate_amount(charged_amount , given_amount)
        self._charged_amount = charged_amount
        self._given_amount = given_amount
    @property 
    def given_amount(self):
        """return given amount"""
        return self._given_amount
    @property
    def charged_amount(self):
        """Return charged amount"""
        return self._charged_amount
    def get_change(self):
        """return the difference between charged and given amount"""
        return self.given_amount - self.charged_amount
    @staticmethod
    def _validate_amount(charged_amount , given_amount):
        """Validate the charged and given amount"""
        if not isinstance(charged_amount , (float , int)) or not isinstance(given_amount , (float , int)):
            raise TypeError("amount must be a integer")
        if charged_amount > given_amount:
            raise ValueError("given amount must be greater or equal to charged amount")
        
    def __str__(self)->str:
        return f"customer gives {self.given_amount} amount and customers charged {self.charged_amount} amount and customer get backs {self.get_change()} amount"
