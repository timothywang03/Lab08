# Lab08Minesweeper.py - Timothy Wang

from graphics import *
from random import randint
from collections import deque
from Button import Button
from UI import UI
from Board import Board, translate

def main():
    ui = UI()
    quit = Button(ui.getWin(), Point(30, 30), 50, 40, 'orange', 'Quit')
    quit.activate()
    cur = ui.getWin().getMouse()
    board = Board()

    while True:
        if quit.clicked(cur):
            ui.getWin().close()
            return

        coords = tuple(int(x) for x in translate(cur.getX(), cur.getY())) #Gets click and converts to grid coords
        if 0 <= coords[0] <= 7 and 0 <= coords[1] <= 7: #If it's on the board
            reveal = board.uncover(coords)
            if reveal == 'Bomb':
                return
            else:
                for x in reveal:
                    ui.board[x[1]][x[0]].undraw()

        cur = ui.getWin().getMouse()

main()
