from graphics import *
from Button import Button


class Square:
    def __init__(self, x, y, win):
        self.x = x
        self.y = y #These are graphical coordinates, translate() will help
        self.win = win
        self.color = 'green' #Initially green


    def set_color(self, newcolor): #Changes the color of the piece
        """Only used on the front-end GUI"""
        self.color = newcolor
        self.button.setColor(newcolor)

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
    def __init__(self):
        self.win = GraphWin('Enter Maze Dimensions', 200, 200)
        x, y = Entry(Point(60, 100), 5), Entry(Point(150, 100), 5)
        x.draw(self.win)
        y.draw(self.win)
        finished = Button(self.win, Point(100, 140), 50, 50, 'green', 'Enter')
        finished.activate()
        quit = Button(self.win, Point(30, 180), 30, 30, 'red', 'Quit')
        quit.activate()

        cur = self.win.getMouse()
        while not quit.clicked(cur):
            if finished.clicked(cur):
                self.x = int(x.getText())
                self.y = int(y.getText())
                self.win.close()
                break
            else:
                self.win.getMouse()

        self.win = GraphWin('Maze', 700, 700)
        self.generate = Button(self.win, Point(40, 40), 50, 25, 'green', 'Generate')
        self.generate.activate()
        self.quit = Button(self.win, Point(120, 40), 50, 25, 'red', 'Quit')
        self.quit.activate()
        cur = self.win.getMouse()

        self.square_size = 700 / self.x // 2

    def get_dimensions(self):
        return self.x, self.y

    def get_win(self):
        return self.win

    def get_quit(self):
        return self.quit

    def get_generate(self):
        return self.generate

UI()
