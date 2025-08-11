from commands.base_command import Command
from drawing.pen import Pen 
class TurnRightCommand(Command):
    def execute(self, pen: Pen):
        pen.turn_right(90)