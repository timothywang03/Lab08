# Lab08Maze.py - Timothy Wang and Darren Shen

from graphics import *
from Maze import Maze
from UIMaze import Square, UI

UI = UI()
maze = Maze(UI.get_dimensions())

cur = UI.get_win().getMouse()

while True:
    if UI.get_quit().clicked(cur):
        UI.get_win().close()

    elif UI.get_generate().clicked(cur):
        
