from copy import deepcopy
class Vector:
    """Represent a Vector in d dimensional space"""
    def __init__(self , d = 3): # default constructor case 
        """Create d-dimensional vector of zeros
        Args:
            d : dimensions of vector. if dimensions not provide its behave like 3D vector  
        """
        # handle copy constructor case :
        if isinstance(d , Vector):
            self._coords = deepcopy(d._coords)
        else:
            self._dimension_validation(d)
            # paramterized constructor 
            self._coords = [0] * d 
    # === magic methods === 
    def __len__(self):
        """Return the dimension of the vector"""
        return len(self._coords)
    def __getitem__(self , j):
        """Return jth coordinate of vector"""
        print("Get item called")
        self._index_validation(j)
        return self._coords[j]
        
    def __setitem__(self , j , value):
        """set jth cordinate of vector to a new value"""
        self._index_validation(j)
        if isinstance(value , (int , float)):
            self._coords[j] = value 
        else:
            raise TypeError("value of vector components should be int or float")
        
    def __add__(self , other):
        """Add two Vectors and return a resultant of addition of two vectors"""
        # checking the vectors length if length is not same through an error
        self._length_validator(other)
        # first create a new vector named-> result of dimensions same as self e.g-> [0,0,0]
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __sub__(self , other) :
        """Substract two vectors"""
        self._length_validator(other)
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result 

    def __eq__(self , other) -> bool:
        """Return True if vector has same cordinates as other"""
        return self._coords == other._coords
    def __ne__(self , other) -> bool :
        """Return True if vector has different coordinates as other"""
        return not self == other # relying on exisitng __eq__ definition
    def __str__(self) -> str :
        """String represenation of nth dimensional vector"""
        return '<' + str(self._coords)[1:-1] + '>'
    def __repr__(self):
        return f"(i , j , k) = {self._coords}"
    
    # === helper methods ===
    def _index_validation(self , j):
        """If member exist in jth index of vector raise index error else not raise error"""
        if not isinstance(j , int):
            raise ValueError("index should be integer type")
        if j >= len(self._coords):
            raise IndexError("Index is out of bonds")
        if j < 0 :
            raise IndexError("Negative indexing is not allowed") 
    def _dimension_validation(self , d):
        """Validate the dimensions of vector"""
        if not isinstance(d , int):
            raise TypeError("Dimensions must be intger type")
    def _length_validator(self , other):
        if len(self) != len(other):
            raise ValueError("dimension must equal for arithmetic operations")


    