from tkinter import Tk, BOTH, Canvas
 

class Window:
    def __init__(self, height, width):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(master=self.root,height=height, width=width)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw(self, line,fill_color):
        line.draw(self.canvas, fill_color)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
       
    def draw(self, canvas,fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y,fill=fill_color, width=2)

class Cell:
    def __init__(self,window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.window = window

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.has_left_wall:
            line_left = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw(line_left, "black")

        if self.has_right_wall:
            line_right = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw(line_right, "black")
        
        if self.has_top_wall:
            line_top = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw(line_top, "black")
        
        if self.has_bottom_wall:
            line_bottom = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw(line_bottom, "black")
        





