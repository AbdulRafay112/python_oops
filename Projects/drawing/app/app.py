import tkinter as tk
from geometry.point import Point 
from drawing.canvas import TKpanel
from drawing.pen import Pen
from geometry.circle import Circle 
class App:
    """Main Application Class for the drawing demo"""
    def __init__(self):
        """Initialize the TKinter windows and canvas"""
        self.root = tk.Tk()
        self.root.title("Abdul Rafay Drawing")
        self.canvas = TKpanel(self.root , width=400 , height=400)
        self.canvas.pack()
    def run(self) -> None :
        """Run the application , demonstrating Poin and Pen Functionality"""
        print("welcome to the oops drawing demonstration")
        # point demo 
        p: Point = Point()
        p.x = 5 
        p.y = 10 
        p.x = 2
        p.y = 3
        q = Point(8,7)
        r = p + q 
        print(f"Point R = P + Q: {r}")
        print(f"X value of R: {r.x}")
        print(f"Y value of R: {r.y}")
        # pen and canvas demo 

        #square
        # ---------------
        pen_1 = Pen(self.canvas)
        pen_1.move_to(50,50)
        pen_1.line_to(150,50)
        pen_1.line_to(150,100)
        pen_1.line_to(50,100)
        pen_1.line_to(50,50)
        # -----------------

        # triangle 
        # --------------
        pen_2 = Pen(self.canvas)
        pen_2.move_to(150,200)
        pen_2.line_to(100,300)
        pen_2.line_to(200,300)
        pen_2.line_to(150,200)
        # -------------------

        # circle demo : draw a circle with center (200,200) with radius 50 
        pen_3 = Pen(self.canvas)
        circle = Circle(Point(300,200) , 50)
        pen_3.draw_circle(circle)
        print("Program completed successfully \n")
        self.root.mainloop()

