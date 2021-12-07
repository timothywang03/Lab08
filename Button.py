from graphics import *


class Button:
    '''Creates a button that can be activated, deactivated, and clicked. Also includes accessors for the label.'''
    def __init__(self, win, center, width, height, color, label):
        self.win = win
        self.center = center
        self.width = width
        self.height = height
        self.color = color
        self.label = label
        self.active = False

        #Construct a rectangle around the center by manipulating the width and height algebraically
        self.button_outline = Rectangle(Point(self.center.getX() - self.width / 2, self.center.getY() - self.height / 2), Point(self.center.getX() + self.width / 2, self.center.getY() + self.height / 2))

        self.button_outline.setFill("gray")
        self.button_text = Text(self.center, str(self.label))
        self.button_outline.draw(self.win)
        self.button_text.draw(self.win)

    def activate(self):
        #Color changes to show when active
        self.button_outline.setFill(self.color)
        self.active = True

    def deactivate(self):
        #Color changes to show when inactive
        self.button_outline.setFill("gray")
        self.active = False

    def getLabel(self):
        return self.label

    def setLabel(self, newText):
        self.label = newText
        self.button_text.setText(newText)
        #Have to change both what is shown and the underlying variable

    def clicked(self, pt):
        #Is a point on the button? A Boolean.
        #ONLY WORKS WHEN ACTIVE
        if self.active:
            if self.center.getX() - self.width / 2 < pt.getX() < self.center.getX() + self.width / 2 and self.center.getY() - self.height / 2 < pt.getY() < self.center.getY() + self.height / 2:
                return True
            else:
                return False
        else:
            return False

    def undraw(self):
        self.button_outline.undraw()
        self.button_text.undraw()

    def setColor(self, newColor):
        if self.active:
            self.color = newColor
            self.button_outline.setFill(newColor)
