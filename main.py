from graphics import Window
from maze import Maze
def main():
    win = Window(800, 600)
    maze = Maze(1,1,10,8,25,25,window=win)
    win.wait_for_close()
main()