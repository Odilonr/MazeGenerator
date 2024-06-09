from tkinter import Tk, BOTH, Canvas
 

class Window:
    def __init__(self, height, width):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas(master=self._root,height=height, width=width)
        self._canvas.pack()
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def draw(self, line,fill_color):
        line.draw(self._canvas, fill_color)
    
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
    
    def close(self):
        self._running = False

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

