from graphics import Window, Line, Point

class Cell:
    def __init__(self,window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._window = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line_left = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw(line_left, "black")

        if self.has_right_wall:
            line_right = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw(line_right, "black")
        
        if self.has_top_wall:
            line_top = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw(line_top, "black")
        
        if self.has_bottom_wall:
            line_bottom = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw(line_bottom, "black")

    def draw_move(self, to_cell, undo=False):
        from_x = (self._x1 + self._x2)/2
        from_y = (self._y1 + self._y2)/2
        to_x = (to_cell._x1 + to_cell._x2)/2
        to_y = (to_cell._y1 + to_cell._y2)/2
        line = Line(Point(from_x,from_y),Point(to_x,to_y))
        if undo:
            self._window.draw(line,"gray")
        else:
            self._window.draw(line,"red")

            

