# Lab08Maze.py - Timothy Wang and Darren Shen

from graphics import *
from collections import deque
from random import randint

class Maze:
    def __init__(self, dimensions):
        self.maze = list(list('C' for x in range(2 * dimensions[0] + 1)) for y in range(2 * dimensions[1] + 1))
        for x in range(len(self.maze)):
            for y in range(len(self.maze[0])):
                if y % 2 == 1 and x % 2 == 1:
                    self.maze[y][x] = 'R'
                if y == 0 or y == len(self.maze[0]) - 1 or x == 0 or x == len(self.maze) - 1:
                    self.maze[y][x] = 'W'

        self.visited = list(list(0 for x in range(2 * dimensions[0] + 1)) for y in range(2 * dimensions[1] + 1))
        j = list(print(x) for x in self.maze)
        print('---------------------------------------------')

        self.path = list()

        self.start, self.end = (1, 1), (len(self.maze) - 2, len(self.maze[0]) - 2)

    def traverse(self, node):
        if node == self.end:
            self.path.append(self.end)
            return 'found'

        open = list()
        for x, y in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
            if 0 <= node[0] + 2 * x < len(self.maze) and 0 <= node[1] + 2 * y < len(self.maze[0]):
                if self.maze[node[0] + x][node[1] + y] != 'W':
                    open.append((node[0] + 2 * x, node[1] + 2 * y))
                    self.maze[node[0] + x][node[1] + y] = 'W'

        while len(open) > 0:
            next_v = open.pop(randint(0, len(open) - 1))

            if self.traverse(next_v) == 'found':
                self.path.insert(0, node)
                return 'found'

    def get_maze(self):
        return self.maze

maze = Maze((10, 10))
maze.traverse((1, 1))
j = list(print(x) for x in maze.get_maze())
print(maze.path)
