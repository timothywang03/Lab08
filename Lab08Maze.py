# Lab08Maze.py - Timothy Wang and Darren Shen

from graphics import *
from Maze import Maze
from UIMaze import UI

def main():
    UI = UI()   # calls the UI class

    cur = UI.get_win().getMouse()   # gets current click

    while True:

        # quit
        if UI.get_quit().clicked(cur):
            UI.get_win().close()

        # if generate is clicked
        elif UI.get_generate().clicked(cur):
            dimensions = UI.get_dimensions()    # grabs dimensions
            maze = Maze(dimensions)
            maze.fill()                         # fills the maze in board module
            maze = maze.get_maze()
            top_left = 350 - (dimensions[0]) * UI.get_square_size() # instantiates top left corner of maze

            # draws the squares within the maze and colors them in
            for x in range(dimensions[0] * 2 + 1):
                for y in range(dimensions[1] * 2 + 1):
                    rect = Rectangle(Point(top_left + x * UI.get_square_size(), top_left + y * UI.get_square_size() + 100),
                                Point(top_left + (x + 1) * UI.get_square_size(), top_left + (y + 1) * UI.get_square_size() + 100))
                    if maze[x][y] == 'W':
                        rect.setFill('brown')
                        rect.setOutline('brown')
                    else:
                        rect.setFill('green')
                        rect.setOutline('green')
                    rect.draw(UI.get_win())

        cur = UI.get_win().getMouse()

main()
