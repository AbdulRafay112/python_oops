from commands.base_command import Command 
from drawing.pen import Pen 
class TurnLeftCommand(Command):
    def execute(self, pen: Pen):
        pen.turn_left(90)