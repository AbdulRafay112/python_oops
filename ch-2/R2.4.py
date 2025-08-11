class Flower:
    """A simple flower Parent or base class that contain flower basic features"""
    def __init__(self , name: str , petals: int , price: float):
        """Inititlze the flower object
        Args: 
             name: the name of the flower 
             petals: petals of the flower 
             price: price of the flower
        """
        if not isinstance(name , str) or not isinstance(petals , int) or not isinstance(price , (float , int)):
            raise TypeError("name should be str type and petals should be int type and price should be float or int type")
        self._name = name 
        self._petals = petals 
        self._price = price 
# === properties ===
    @property 
    def name(self) -> str:
        """Return the name of the flower"""
        return self._name 
    @name.setter 
    def name(self , value) -> None :
        """Set the name of the flower by new name"""
        self.name = value
    @property 
    def petals(self) -> int :
        """Return the petals of flower"""
        return self._petals 
    @petals.setter 
    def petals(self , amount) -> None :
        """Set the petals by new amount"""
        self._petals = amount 
    @property 
    def price(self) -> float :
        """Get Price of flower"""
        return self._price 
    @price.setter 
    def price(self , new_price) -> None:
        """Setting price of flower by new price""" 
        self._price = new_price 
    
