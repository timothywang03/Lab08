# Lab08Minesweeper.py - Timothy Wang and Darren Shen

from graphics import *
from random import randint
from collections import deque
from Button import Button
from UIMinesweeper import UI
from Board import Board, translate

def main():

    # initializes classes
    board = Board()
    ui = UI(board.get_board())

    # activates quit button
    quit = Button(ui.getWin(), Point(30, 30), 50, 40, 'orange', 'Quit')
    quit.activate()

    # generates title
    title = Text(Point(300, 50), 'Minesweeper')
    title.setSize(30)
    title.draw(ui.getWin())

    # generates instructions
    instructions = Text(Point(300, 80), "Click a tile to select it, then press 'F' to flag or 'D' to dig up")
    instructions.setSize(10)
    instructions.draw(ui.getWin())

    cur1 = ui.getWin().getMouse()

    endgame = True # boolean for win or loss

    # game loop
    while True:

        # exit if quit is clicked
        if quit.clicked(cur1):
            ui.getWin().close()
            return

        # gets the key for secondary command
        cur2 = ui.getWin().getKey()
        coords = tuple(int(x) for x in translate(cur1.getY(), cur1.getX())) # converts click to grid coordinates
        if 0 <= coords[0] <= 7 and 0 <= coords[1] <= 7: # checks bounds
            if cur2 == 'f':    # flagging a tile makes it red
                if ui.get_board()[coords[0]][coords[1]].get_color() == 'green':
                    ui.board[coords[0]][coords[1]].set_color('red')
                else:
                    ui.board[coords[0]][coords[1]].set_color('green')
            else:
                reveal = board.uncover(coords)
                if reveal == 'Bomb':    # bomb is clicked --> loss
                    endgame = False
                    break
                else:
                    for x in reveal:    # undraws all the squares that are uncovered
                        ui.get_board()[x[0]][x[1]].undraw()

        counter = 0     # keeps track of how many tiles have been removed
        for x in board.get_covered():
            for y in x:
                if y == 1:
                    counter += 1

        if counter == 54:
            endgame == True
            break

        cur1 = ui.getWin().getMouse()

    if endgame is True:
        title.setText('You Won! Play Again?')
    else:
        title.setText('You Lost! Play Again?')
        for x in board.get_mines():
            Text(Point(125 + 50 * x[1], 125 + 50 * x[0]), 'M').draw(ui.getWin())

    # initalizes replay button
    replay = Button(ui.getWin(), Point(90, 30), 50, 40, 'orange', 'Replay')
    replay.activate()
    cur1 = ui.getWin().getMouse()

    while True:
        if replay.clicked(cur1):    # creates a new game in a new window
            ui.getWin().close()
            main()
            break
        elif quit.clicked(cur1):
            break

main()
