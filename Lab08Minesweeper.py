# Lab08Minesweeper.py - Timothy Wang

from graphics import *
from random import randint
from collections import deque
from Button import Button
from UI import UI
from Board import Board, translate

def main():
    board = Board()
    ui = UI(board.get_board())
    quit = Button(ui.getWin(), Point(30, 30), 50, 40, 'orange', 'Quit')
    quit.activate()

    title = Text(Point(300, 50), 'Minesweeper')
    title.setSize(30)
    title.draw(ui.getWin())

    instructions = Text(Point(300, 80), "Click a tile to select it, then press 'F' to flag or 'D' to dig up")
    instructions.setSize(10)
    instructions.draw(ui.getWin())
    cur1 = ui.getWin().getMouse()
    flagged = list()

    endgame = True

    j = list(print(x) for x in board.get_board())
    while True:
        if quit.clicked(cur1):
            ui.getWin().close()
            print('fjdkfj')
            return

        cur2 = ui.getWin().getKey()
        coords = tuple(int(x) for x in translate(cur1.getY(), cur1.getX())) #Gets click and converts to grid coords
        if 0 <= coords[0] <= 7 and 0 <= coords[1] <= 7: #If it's on the board
            if cur2 == 'f':
                if ui.get_board()[coords[0]][coords[1]].get_color() == 'green':
                    ui.board[coords[0]][coords[1]].set_color('red')
                else:
                    ui.board[coords[0]][coords[1]].set_color('green')
            else:
                reveal = board.uncover(coords)
                if reveal == 'Bomb':
                    endgame = False
                    break
                else:
                    for x in reveal:
                        ui.get_board()[x[0]][x[1]].undraw()

        counter = 0
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
    replay = Button(ui.getWin(), Point(90, 30), 50, 40, 'orange', 'Replay')
    replay.activate()
    cur1 = ui.getWin().getMouse()

    while True:
        if replay.clicked(cur1):
            ui.getWin().close()
            main()
            break
        elif quit.clicked(cur1):
            break

main()
