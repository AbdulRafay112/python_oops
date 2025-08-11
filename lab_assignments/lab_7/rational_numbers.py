from __future__ import annotations
from math import gcd 
class RationalNumber:
    """Simple Rational Numbers Class that handle all operations related to Rational Numbers"""
    def __init__(self , numerator: int , denominator: int):
        """Constructor of Rational Numbers Class , inititalze class with arguments numerator and denominator
        Args:
            numerator: Fraction upper Element , type -> float
            denominator: Fraction downward element , type -> float 
        """
        if denominator == 0 :
            raise ValueError("Denominator Can not be Zero")
        if not isinstance(numerator , int) or not isinstance(denominator , int):
            raise TypeError("Numerator and denominator should be integer type")
        self._numerator = numerator
        self._denominator = denominator 
        self.simplify()


    # === getter and setter methods ===
    @property 
    def numerator(self) -> int :
        """Get the numerator"""
        return self._numerator
    @numerator.setter 
    def numerator(self , value: int) -> None :
        """Set Numerator by a new value"""
        if isinstance(value , int):
            self._numerator = value 
        else:
            raise TypeError("Numerator should be integer type")
    @property 
    def denominator(self) -> int :
        """get the value of denominator"""
        return self._denominator 
    @denominator.setter
    def denominator(self , value: int) -> None:
        """Set the value of denominator by a new value"""
        if not isinstance(value , int):
            raise TypeError("denominator should be integer type")
        elif value == 0 :
            raise ValueError("denominator can not be zero")
        self._denominator = value 

    # === operator overloading === 
    def __add__(self , other: RationalNumber) -> RationalNumber:
        """Add two Rational Numbers and return new rational number of two rational numbers addition result"""
        new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        return RationalNumber(new_numerator , new_denominator)
    def __sub__(self , other: RationalNumber) -> RationalNumber:
        """Subtract two rational numbers"""
        new_numerator = self._numerator * other._denominator - other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator 
        return RationalNumber(new_numerator , new_denominator)
    def __mul__(self , other: RationalNumber) -> RationalNumber:
        """Multiply two rational numbers"""
        return RationalNumber(self._numerator * other._numerator , self._denominator * other._denominator)
    def __truediv__(self , other: RationalNumber) -> RationalNumber:
        """Divide two rational numbers"""
        if other._numerator == 0 :
            raise ValueError("Can not divide by zero")
        return RationalNumber(self._numerator * other._denominator , self._denominator * other._numerator)
     
    def simplify(self) -> None:
        """simplifies the fraction to its lowest form"""
        common_divisor = gcd(self._numerator , self._denominator)
        self._numerator //= common_divisor 
        self._denominator //= common_divisor 
        if self._denominator < 0:
            self._numerator *= -1
            self._denominator *= -1

    
    # === string representation ===
    def __str__(self) -> str:
        return f"{self._numerator} / {self._denominator}" 
        