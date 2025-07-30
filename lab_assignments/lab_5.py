import math
class Triangle:
    """basic triangle with 3 perimeters A , B , C  with basics methods"""

    """Defining class variable"""
    _object_count: int = 0 # to track object count

    def __init__(self , *args):
        # defining the constructor : 
        print("constructor called")
        Triangle._object_count += 1 
        # if no argument given every variable assigns to 1.0 
        if len(args) == 0 :
            self._side_a = self._side_b = self._side_c = 1.0 
        elif len(args) == 1 and isinstance(args[0] , (int , float)):
            self._side_a = self._side_b = self._side_c = float(args[0])
        elif len(args) == 2 :
            x , y = args 
            self._side_a = self._side_b = float(x)
            self._side_c = float(y)
        elif len(args) == 3:
            self._side_a , self._side_b , self._side_c = map(float , args)
        elif len(args) == 1 and isinstance(args[0] , Triangle):
            other = args[0]
            self._side_a = other._side_a 
            self._side_b = other._side_b 
            self._side_c = other._side_c
        else:
            raise ValueError("Invalid Constructor Arguments")

    # methods
    # set methods
    @property 
    def side_a(self) -> float:
        """Returning side a"""
        return self._side_a 
    @property
    def side_b(self) -> float:
        """Returning side b"""
        return self._side_b 
    @property
    def side_c(self) -> float:
        """Returning side c"""
        return self._side_c 
    # get methods 
    @side_a.setter 
    def side_a(self , value: float) -> None :
        """Setting value for perimter a """
        self._side_a = value 
    @side_b.setter 
    def side_b(self , value: float) -> None :
        """setting value for perimter b"""
        self._side_b = value 
    @side_c.setter 
    def side_c(self , value: float) -> None :
        """setting value for perimter c"""
        self._side_c = value 
    # class method 
    @classmethod
    def object_count(cls) -> int:
        """Returning object count how many object is created from this class"""
        return cls._object_count
    # instance methods 
    def perimeter(self) -> float:
        """calculating the sum of perimeters of triangle"""
        return self._side_a + self._side_b + self._side_c 
    def is_right_angled(self) -> bool :
        """Checking if the triangle is right angle or not"""
        sides = sorted([self._side_a , self._side_b , self._side_c])
        return math.isclose(sides[0]**2 + sides[1]**2 , sides[2]**2)
    # string representation 
    def __str__(self) -> str:
        return f"Triangle sides are A = {self._side_a} , B = {self._side_b} , C={self._side_c}"


    
t4 = Triangle(3,4,5)
t5 = Triangle(t4) 
t4.side_a = 9
print(t4)
print(t5)





    



  
    


