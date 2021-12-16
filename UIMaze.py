from graphics import *
from Button import Button


class UI:
    def __init__(self):
        # starting screen where user enters dimensions
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

                # instantiates dimensions of grid
                self.x = int(x.getText())
                self.y = int(y.getText())
                if 1 <= self.x < 30 and 1 <= self.y < 30:
                    self.win.close()
                    break
                else:
                    pass
            else:
                self.win.getMouse()
            cur = self.win.getMouse()

        # instantiates all the ui elements needed to create maze
        self.win = GraphWin('Maze', 700, 800)
        self.generate = Button(self.win, Point(40, 40), 50, 25, 'green', 'Generate')
        self.generate.activate()
        self.quit = Button(self.win, Point(120, 40), 50, 25, 'red', 'Quit')
        self.quit.activate()

        self.square_size = 600 // (max(self.x, self.y) * 2 + 1)

    def get_dimensions(self):
        return self.x, self.y

    def get_win(self):
        return self.win

    def get_quit(self):
        return self.quit

    def get_generate(self):
        return self.generate

    def get_square_size(self):
        return self.square_size
