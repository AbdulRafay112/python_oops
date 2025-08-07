from geometry.point import Point 
from typing import List 
import math 

class Circle:
    """A circle is defined by a center point and radius"""
    def __init__(self , center: Point , radius: float):
        """Initialize a circle with center point and radius
        Args:
            center: A Point object representing the circles center 
            radius: float representing the circle radius
        """
        if not isinstance(center , Point):
            raise TypeError("Center must be Point class object")
        if not isinstance(radius , (int , float)) and radius <= 0 :
            raise ValueError("radius must be a number")
        self._center = center 
        self._radius = radius 

    @property
    def center(self) -> Point :
        """Get center of the circle"""
        return self._center 
    @center.setter 
    def center(self , value: Point) -> None : 
        """Set center of the circle"""
        if isinstance(value , Point):
            self._center = value 
        else:
            raise TypeError("Value must be Point type")
    @property
    def radius(self) -> float:
        """Get radius of the circle"""
        return self._radius 
    @radius.setter 
    def radius(self , value: float) -> None:
        if isinstance(value , (int , float)) :
            self._radius = float(value)
        else:
            raise TypeError("value must be int or float type")
    # === get_points method ===
    def get_points(self , num_points: int = 100) -> List[Point]:
        """Generate Points on the circle circumference
        Args:
            num_points: number of points to approximate the circle
        Returns:
            list of Point objects on the circle circumference
        """
        points = []
        for i in range(num_points) :
            angle = 2 * math.pi * i / num_points
            x = self._center.x + self._radius * math.cos(angle)
            y = self._center.y + self._radius * math.sin(angle)
            points.append(Point(x , y))
        return points 
    def __str__(self) -> str:
        """string representation"""
        return f"Circle (center = {self._center} , radius = {self._radius})"

         