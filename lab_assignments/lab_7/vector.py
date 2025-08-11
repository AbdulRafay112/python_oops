from __future__ import annotations
from math import sqrt
class Vector:
    """A simple 2D Vector Class of handling the basic features of 2D Vector"""
    def __init__(self , x: float , y: float):
        """Initializing 2D Vector Class 
        Args:
            x: x-component of vector mainly written as coefficient of i^
            y: y-componennt of vector mainly written as coefficient of j^
        """
        if not isinstance(x , (int , float)) or not isinstance(y , (int , float)) :
            raise TypeError("X or Y must be integer or float")
        self._x = x
        self._y = y 
    # === properties === 
    @property 
    def x(self) -> float :
        """Get x cordinate of vector"""
        return self._x 
    @x.setter 
    def x (self , value) -> None:
        """Set x cordinate of vector to a new value """
        if not isinstance(value , (int , float)):
            raise ValueError("X should be int or float type")
        self._x = value 
    @property 
    def y(self) -> float :
        """Get y cordinate of vector"""
        return self._y 
    @x.setter 
    def x (self , value) -> None:
        """Set y cordinate of vector to a new value """
        if not isinstance(value , (int , float)):
            raise ValueError("y should be int or float type")
        self._y = value 
    # === operator overloading === 
    def __add__(self , other:Vector) -> Vector :
        """Add two vectors"""
        return Vector(self._x + other._x , self._y + other._y)
    def __sub__(self , other: Vector) -> Vector:
        """SUbstract two vectors"""
        return Vector(self._x - other._x , self._y - other._y)
    def dot_product(self , other: Vector) -> float:
        """Calculate the dot product of two vectors""" 
        return self._x * other._x + self._y * other._y 
    def magnitude(self) -> float:
        """Calculate the magnitude of vector"""
        return sqrt(self._x**2 + self._y**2)
    def __str__(self) -> str :
        return f"({self._x} , {self._y})"

    

    
