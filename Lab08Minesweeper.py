# Lab08Minesweeper.py - Timothy Wang

from graphics import *
from random import randint
from collections import deque

class Board:
    def __init__(self):
        # initalizes 8x8 board
        self.board = list(list(None for x in range(8)) for y in range(8))

        # initalizes a list of 10 mines, generated at random with no overlap
        self.mines = list()
        for x in range(10):
            mine = (randint(0, 7), randint(0, 7))
            if mine not in self.mines:
                self.mines.append(mine)
            else:
                continue

        # places the mines onto the board
        for x in self.mines:
            self.board[x[0]][x[1]] = 'M'

        # for each grid space, check adjacent 8 tiles to see if there are mines, and assign appropriate number
        for x in range(8):
            for y in range(8):
                if (x, y) not in self.mines:
                    adjacent = 0
                    for direction in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 1), (-1, 0)]:    # refers to each cardinal direction
                        new_x, new_y = x + direction[0], y + direction[1]   # updates coordinates to peek, but doesn't traverse
                        if 0 <= new_x < 8 and 0 <= new_y < 8:   # checks bounds to make sure peeking doesn't go beyond boundaries
                            if self.board[new_x][new_y] == 'M':
                                adjacent += 1
                    self.board[x][y] = str(adjacent)
        j = list(print(x) for x in self.board)
        print(self.mines)
        self.covered = list(list(0 for x in range(8)) for y in range(8))

    def uncover(self, space):
        """Given a space that is clicked, will return and output a list of all tiles that will be uncovered

        :param space: a tuple with the format (y coordinate, x coordinate) that initial space clicked
        :returns: a list with length >= 1 of all uncovered tiles or 'Bomb'"""
        queue = deque() # initializes a deque, but will only be used like a queue; TODO: change to implement non-built-in or ask Kashiwada
        path = list()
        queue.append(space)

        # graph floodfill algorithm that uses BFS to search through and locate an area of 0's
        while len(queue) > 0:   # loop will end when there are no more spaces in the queue, which also means an area has been found
            cur = queue.popleft()
            path.append(cur)

            if self.board[cur[0]][cur[1]] == 'M':   # immediately returns bomb if a bomb is clicked; this case will only run on 0th iteration of BFS
                return 'Bomb'
            elif self.board[cur[0]][cur[1]] != '0': # passes if a tile that has a bomb adjacent is traversed; aka a number tile has been hit
                pass
            else:
                for x, y in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 1), (-1, 0)]: # searches all 8 cardinal directions
                    new_x, new_y = cur[0] + x, cur[1] + y
                    if 0 <= new_x < 8 and 0 <= new_y < 8:   # checks bounds on the new coordinates
                        if self.covered[new_x][new_y] == 0: # makes sure that coordinates haven't already been traversed
                            queue.append((new_x, new_y))
                            self.covered[new_x][new_y] = 1
        self.covered[space[0]][space[1]] = 1
        return path


board = Board()
j = list(print(x) for x in board.board)
print(board.uncover((4, 4)))
