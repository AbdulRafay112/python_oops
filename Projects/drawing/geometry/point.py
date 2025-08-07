from __future__ import annotations
from typing import Union 
class Point:
    """A 2D Point class with x and y co-ordinates , supporting addition and distance calculations"""

    """A class Variable to track Point instances"""
    count: int = 0 

    def __init__(self , x: Union[Point , float] = 0.0 , y: float = 0.0 ):
        """
        Initialize a point object
        Args:
           x is float for x _cordinate and Point for copy constructor case
           y is float incase of y_cordinate , ignore if x is a Point
        A simple constructor for point class with : 
        default constructor = Point()
        parameterized constructor=Point(x , y)
        copy constructor: Point(p1:Point)
        """
        if isinstance(x , Point):
            self._x = x._x 
            self._y = x._y 
            print("Copy constructor invoked")
        else:
            if not isinstance(x , (int , float)) or not isinstance(y , (int , float)):
                raise TypeError("x and y must be int or float type")
            self._x = x 
            self._y = y 
            
        Point.count += 1 

    # === properties === 
    @property
    def x(self) -> float :
        """Get the x co-ordinate"""
        return self._x 
    @x.setter
    def x(self , value: float) -> None :
        """Set value of x co-ordinate to a new value"""
        if isinstance(value , (int , float)):
            self._x = float(value) 
        else:
            raise TypeError("new value of x must be int or float")
    @property
    def y(self) -> float :
        """Get value of y co-ordinate"""
        return self._y 
    @y.setter 
    def y(self , value: float) -> None:
        """Set value of y to a new value"""
        if isinstance(value , (int , float)):
            self._y = float(value) 
        else:
            raise TypeError("new value of y must be int or float")
    
    # === operator overloading === 
    def add(self , other: Point) -> Point:
        """Add two co-ordinates x and y , x of one should be add to x of other and y of one should be add to y of other"""
        if isinstance(other , Point):
            return Point(self._x + other._x , self._y + other._y)
        else:
            raise TypeError("Only same class instance must be add to other")
     # === magic method ===
    def __add__(self , other: Point) -> Point:
        return self.add(other)
    
    # === distance calculator between two points ===
    def distance(self , other: Point) -> float :
        """Return the total distance between two points"""
        if isinstance(other , Point):
            result = ((self._x - other._x)**2 + (self._y - other._y)**2 ) **0.5 
        else:
            raise TypeError("calculate distance for only same instance e.g-> Point")
        return float(result)
    # string representation for user 
    def __str__(self) -> str:
        return f"{self._x} -- {self._y}"
    # developer representation
    def __repr__(self) -> str :
        return f"x = {self._x} and y = {self._y}"
    
    # === equlancy overloading === 
    def __eq__(self , other: Point) -> bool :
        if isinstance(other , Point):
            return self._x == other._x and self._y == other._y      
        else:
            raise TypeError("instances must be of same type")
    
    @classmethod
    def get_instance_count(cls) -> int:
        """Get the total number of Point instances"""
        return cls.count 
