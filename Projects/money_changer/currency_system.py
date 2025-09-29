class CurrencySystem:
    """This class represents the currency denominations"""
    def __init__(self , denominations):
        # sorted denomination in to descending order
        self._denomination_validator(denominations)
        self._denominations = sorted(denominations , reverse=True)
    @property
    def denominations(self):
        """Return the currency denominations"""
        return self._denominations
    @staticmethod
    def _denomination_validator(denominations):
        if not isinstance(denominations , list):
            raise TypeError("denominations must be provided in a list")
        if not denominations: # checking if denomination is empty 
            raise ValueError("denominations list can not be empty")
    def __str__(self)->str:
        return f"denominations are {self.denominations}"
        
    
