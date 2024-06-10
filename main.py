from graphics import Window
from maze import Maze
def main():
    win = Window(800, 600)
    maze = Maze(1,1,10,10,100,100,window=win)
    maze.solve()
    win.wait_for_close()
main()