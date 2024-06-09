from tkinter import Tk, BOTH, Canvas

def main():
    win = Window(800, 600)
    win.draw(Line(Point(0,0),Point(100,234)),"red")
    win.wait_for_close()
 

class Window:
    def __init__(self, height, width):
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title("Maze Solver")
        self.canvas = Canvas(master=self.root, background='black')
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
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y
       
    def draw(self, canvas,fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2,fill=fill_color, width=2)






main()





