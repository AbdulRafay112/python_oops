from geometry.point import Point 
from geometry.circle import Circle
class Pen :
    """A pen for drawing lines on a TK panel"""
    def __init__(self , canvas):
        """ Initialize the pen with canvas 
        Args: TK panel object to draw on
        """
        self._canvas = canvas 
        self._cp = Point(0,0) # current position
        self._angle = 0 

    # === move_to function ===
    def move_to(self , x: float , y:float) -> None :
        """Move a pen to a new position with out drawing"""
        self._cp = Point(x,y)
    # === line_to function ===
    def line_to(self , x: float , y: float) -> None :
        """Draw a line from current position to a new point"""
        new_point = Point(x,y)
        self._canvas.add_line(self._cp , new_point)
        self._cp = new_point


    def draw_circle(self , circle: Circle) -> None :
        """Draw a circle by connecting its points on its circumference
        Args:
            circle: circle object to draw
        """
        if not isinstance(circle , Circle):
            raise TypeError("circle must be Circle type")
        points = circle.get_points()
        self.move_to(points[0].x , points[0].y)
        for point in points[1:] :
            self.line_to(point.x , point.y)
        self.line_to(points[0].x , points[0].y)  #close the circle 
        

    def get_position(self) -> Point:
        """Get teh current position of the pen"""
        return self._cp 
    
    def turn_right(self , degrees: float) -> None :
        self._angle = (self._angle - degrees) % 360 
    def turn_left(self , degrees: float) -> None:
        self._angle = (self._angle + degrees) % 360 
    def get_angle(self) -> float :
        return self._angle 