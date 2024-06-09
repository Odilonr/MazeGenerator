from graphics import Window
from maze import Maze
def main():
    win = Window(800, 600)

    maze = Maze(0,0,100,120,100,100,win)
    win.wait_for_close()
main()