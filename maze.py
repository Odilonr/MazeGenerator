from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self.seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                row.append(Cell(self._window))
            self._cells.append(row)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._window is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._window is None:
            return
        self._window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            need_visitation = []
            if i > 0 and not self._cells[i-1][j].visited:
                need_visitation.append((i-1,j))
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                need_visitation.append((i+1,j))
            if j < self._num_rows - 1  and not self._cells[i][j+1].visited:
                need_visitation.append((i,j+1))
            if j > 0 and not self._cells[i][j-1].visited:
                need_visitation.append((i,j-1))
            if len(need_visitation) == 0:
                self._draw_cell(i,j)
                return
            index = random.randrange(len(need_visitation))
            random_cell = need_visitation[index]

            if random_cell[1] == j + 1:
                self._cells[i][j+1].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False

            if random_cell[1] == j - 1:
                self._cells[i][j-1].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False

            if random_cell[0] == i + 1:
                self._cells[i+1][j].has_left_wall = False
                self._cells[i][j].has_right_wall = False

            if random_cell[0] == i - 1:
                self._cells[i-1][j].has_right_wall = False
                self._cells[i][j].has_left_wall = False

            self._break_walls_r(random_cell[0],random_cell[1])
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _solve_r(self,i,j):
        self._animate()

        self._cells[i][j].visited = True

        if i == self._num_cols-1 and  j == self._num_rows-1:
            return True
        
        if i > 0 and not self._cells[i-1][j].visited and not self._cells[i-1][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo= True)

        if i < self._num_cols - 1 and not self._cells[i+1][j].visited and not self._cells[i+1][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],undo = True)

        if j > 0 and not self._cells[i][j-1].visited and not self._cells[i][j-1].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo = True)

        if j < self._num_rows - 1 and not self._cells[i][j+1].visited and not self._cells[i][j+1].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo = True)

        return False
        
    def solve(self):
        return self._solve_r(0,0)

        

            


                
