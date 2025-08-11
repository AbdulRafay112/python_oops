from drawing.pen import Pen 
class Command:
    """Base class for different command instances"""
    def execute(self , pen: Pen):
        """Implemented in childrens"""
        pass 