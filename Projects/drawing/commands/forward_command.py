import math 
from commands.base_command import Command
from drawing.pen import Pen 

class ForwardCommand(Command):
    """Command for forward the line"""
    def __init__(self , distance = 50):
        """Initialize the forward command with distance = 50"""
        self._distance = distance 
    def execute(self , pen: Pen):
        """Function for executing forward command"""
        x = pen.get_position().x
        y = pen.get_position().y 
        angle_rad = math.radians(pen.get_angle())
        new_x = x + self._distance * math.cos(angle_rad)
        new_y = y + self._distance * math.sin(angle_rad)
        pen.line_to(new_x , new_y)


