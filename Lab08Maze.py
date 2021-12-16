# Lab08Maze.py - Timothy Wang and Darren Shen

from graphics import *
from Maze import Maze
from UIMaze import UI

def main():
    ui = UI()   # calls the ui class

    cur = ui.get_win().getMouse()   # gets current click

    while True:

        # quit
        if ui.get_quit().clicked(cur):
            ui.get_win().close()
            break

        # if generate is clicked
        elif ui.get_generate().clicked(cur):
            dimensions = ui.get_dimensions()    # grabs dimensions
            maze = Maze(dimensions)
            maze.fill()                         # fills the maze in board module
            maze = maze.get_maze()
            top_left = 350 - (dimensions[0]) * ui.get_square_size() # instantiates top left corner of maze

            # draws the squares within the maze and colors them in
            for x in range(dimensions[0] * 2 + 1):
                for y in range(dimensions[1] * 2 + 1):
                    rect = Rectangle(Point(top_left + x * ui.get_square_size(), top_left + y * ui.get_square_size() + 100),
                                Point(top_left + (x + 1) * ui.get_square_size(), top_left + (y + 1) * ui.get_square_size() + 100))
                    if maze[y][x] == 'W':
                        rect.setFill('brown')
                        rect.setOutline('brown')
                    else:
                        rect.setFill('green')
                        rect.setOutline('green')
                    rect.draw(ui.get_win())

        cur = ui.get_win().getMouse()

main()
