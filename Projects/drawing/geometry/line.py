from geometry.point import Point
class Line:
    """A line segment defined by two Points"""
    def __init__(self , start: Point , end: Point):
        """Initialize a line with start and end points.
        Args:
            start: Starting point of the line
            end: Ending point of the line
        """
        if isinstance(start , Point) and isinstance(end , Point):
            self.start = start 
            self.end = end 
        else:
            raise TypeError("Start and End Point Must be Point class instances")
    
    # === length function for line ===
    def length(self) -> float :
        """Calculate length of the line"""
        return self.start.distance(self.end)
    # === string representation === 
    def __str__(self) -> str :
        """Print for user (magic method)"""
        return f"Line: from {self.start} to {self.end}"
