from __future__ import annotations
from copy import deepcopy
from math import gcd 
class RationalNumber:
    """Simple Rational Numbers Class that handle all operations related to Rational Numbers"""
    def __init__(self , numerator: int = 0 , denominator: int = 1): # default constructor logic handling 
        """Constructor of Rational Numbers Class , inititalze class with arguments numerator and denominator
        Args:
            numerator: Fraction upper Element , type -> float
            denominator: Fraction downward element , type -> float 
        """
        if isinstance(numerator , RationalNumber):
            """Copy constructor case handling"""
            self._numerator , self._denominator = numerator._numerator , numerator._denominator
        else:
            if isinstance(numerator , tuple):
                if len(numerator) != 2 :
                    raise ValueError("Fraction must include two parts e.g -> numerator , denominator")
                numerator , denominator = numerator
            self._validate_denominator(denominator)
            numerator , denominator = self._normalize_sign(numerator , denominator)
            numerator , denominator = self._simplify(numerator , denominator)
            self._numerator = numerator
            self._denominator = denominator 
    @classmethod
    def from_string(cls , fraction_str: str) :
        parts = fraction_str.split("/")
        if len(parts) != 2 :
            raise ValueError("fraction must include two parts")
        num , den = int(parts[0]) , int(parts[1])
        return cls(num , den) 


    # === getter methods we donot need setter function because denominator and numerator are immutable ===
    @property 
    def numerator(self) -> int :
        """Get the numerator"""
        return self._numerator
    @property 
    def denominator(self) -> int :
        """get the value of denominator"""
        return self._denominator 

    # === operator overloading === 
    def __add__(self , other) -> RationalNumber:
        """Add two Rational Numbers and return new rational number of two rational numbers addition result"""
        num = self._numerator * other._denominator + self._denominator * other._numerator
        den = self._denominator * other._denominator 
        return RationalNumber(num , den)
    
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
     
    def _validate_denominator(self , denominator: int) -> None:
        """Validate the denominator if denominator is 0 raise value error"""
        if denominator == 0 :
            raise ZeroDivisionError("denominator can not be zero")
    def _normalize_sign(self , numerator: int , denominator: int) -> tuple:
        return (-numerator , -denominator) if denominator < 0 else (numerator , denominator)
    def _simplify(self , numerator: int , denominator: int) -> tuple :
        """Simplify the fraction term in to its lowest form like 8 / 6 lowest form is 4 / 3"""
        if numerator == 0 :
            return 0 , denominator
        hcf = gcd(numerator , denominator)
        return numerator // hcf , denominator // hcf 

     # === string representation ===
    def __str__(self) -> str:
        return f"{self._numerator} / {self._denominator}" 



r1 = RationalNumber(1,2)
r2 = RationalNumber(3,4)
r3 = r1 + r2
print(r3)
