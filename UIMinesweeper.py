from graphics import *
from Button import Button


class Square:
    def __init__(self, x, y, win, button):
        self.x = x
        self.y = y  # These are graphical coordinates, translate() will help
        self.win = win
        # We make it a button so that it can be clicked
        self.button = button(self.win, Point(
            self.x, self.y), 50, 50, 'green', '')
        self.button.activate()
        self.color = 'green'  # Initially green

    def set_color(self, newcolor):  # Changes the color of the piece
        """Only used on the front-end GUI"""
        self.color = newcolor
        self.button.setColor(newcolor)

    def is_clicked(self, mouse_click):
        # Boolean, checks if button clicked
        return self.button.clicked(mouse_click)

    def undraw(self):
        self.button.undraw()

    # Getter methods below:

    def get_color(self):
        return self.color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_win(self):
        return self.win


class UI:
    def __init__(self, board):
        self.win = GraphWin('Minesweeper', 600, 600)    # initalizes window

        # sets background color
        background = Rectangle(Point(-1, -1), Point(601, 601))
        background.setFill('#D2B48C')
        background.draw(self.win)

        # saves all button within matrix
        self.board = list()
        for x in range(8):
            row = list()
            for i in range(8):
                if str(board[x][i]) != '0':
                    Text(Point(125 + 50 * i, 125 + 50 * x),
                         str(board[x][i])).draw(self.win)
                # Creates square objects within the board list, a list-of-lists that allows us to access squares by coords
                row.append(Square(125 + 50 * i, 125 +
                           50 * x, self.win, Button))
            self.board.append(row)

    def getWin(self):
        """Returns window"""
        return self.win

    def get_board(self):
        """Returns board matrix"""
        return self.board
