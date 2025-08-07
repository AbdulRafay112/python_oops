import tkinter as tk 
from geometry.point import Point 
from geometry.line import Line 
class TKpanel(tk.Canvas):
    """A tkinter canvas for drawing line"""
    def __init__(self , master=None , width: int = 400 , height: int = 400 , **kwargs):
        """Initialze the TK panel
        Args:
            master: Parent tkinter widget
            width: Canvas width in pixels 
            height: Canvas height in pixels 
            **kwargs: Additional tkinter Canvas Argument
        """
        super().__init__(master , width = width , height= height , bg='white' , **kwargs)
        self.lines: list[Line] = []
    # === add line function === 
    def add_line(self , p1: Point , p2: Point) -> None :
        """Add a line to the canvas and draw it"""
        if isinstance(p1 , Point) and isinstance(p2 , Point):
            self.lines.append(Line(p1 , p2))
            print(f"Line from ({p1.x} , {p1.y}) to ({p2.x} , {p2.y})")
            self.draw()
        else:
            raise TypeError("starting and ending points must be Point class")
    def draw(self) -> None :
        """Draw all stored lines on the canvas"""
        self.delete('all') # clear previous drawing
        for line in self.lines:
            self.create_line(line.start.x , line.start.y , line.end.x , line.end.y , fill='black' , width=2)