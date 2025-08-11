from rational_numbers import RationalNumber 
from vector import Vector 

if __name__ == "__main__":
    # Rational Number Example
    r1: RationalNumber = RationalNumber(1, 2)
    r2: RationalNumber = RationalNumber(3, 4)
    print("Rational Add:", r1 + r2)
    print("Rational Subtract:", r1 - r2)
    print("Rational Multiply:", r1*r2)
    print("Rational Divide:", r1 / r2)

    # Vector2D Example
    v1: Vector = Vector(2, 3)
    v2: Vector = Vector(4, 5)
    print("Vector Add:", v1 + v2)
    print("Vector Subtract:", v1 - v2)
    print("Dot Product:", v1.dot_product(v2))
    print("Magnitude of v1:", v1.magnitude())
