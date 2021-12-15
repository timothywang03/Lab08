from random import randint

class Maze:
    def __init__(self, dimensions):
        self.maze = list(list('W' for x in range(2 * dimensions[0] + 1)) for y in range(2 * dimensions[1] + 1))
        for x in range(len(self.maze)):
            for y in range(len(self.maze[0])):
                if y % 2 == 1 and x % 2 == 1:
                    self.maze[y][x] = 'R'
                if y == 0 or y == len(self.maze[0]) - 1 or x == 0 or x == len(self.maze) - 1:
                    self.maze[y][x] = 'W'

        self.visited = list(list(0 for x in range(dimensions[1])) for y in range(dimensions[0]))

        self.adjacency = dict()
        for x in range(dimensions[0]):
            for y in range(dimensions[1]):
                self.adjacency[(x, y)] = list()

    def traverse(self, node):
        open = list()
        for x, y in [(0, 1), (-1, 0), (0, -1), (1, 0)]: # for all the adjacent rooms
            if 0 <= node[0] + 2 * x < len(self.maze) and 0 <= node[1] + 2 * y < len(self.maze[0]):
                if self.visited[node[0] // 2 + x][node[1] // 2 + y] == 0:
                    open.append((node[0] + 2 * x, node[1] + 2 * y))
                    self.visited[node[0] // 2 + x][node[1] // 2 + y] = 1

        while len(open) > 0:
            next_v = open.pop(randint(0, len(open) - 1))
            self.adjacency[(node[0] // 2, node[1] // 2)].append((next_v[0] // 2, next_v[1] // 2))
            self.adjacency[(next_v[0] // 2, next_v[1] // 2)].append((node[0] // 2, node[1] // 2))
            self.traverse(next_v)

    def fill(self):
        self.traverse((1, 1))
        for x, y in self.adjacency.items():
            for z in y:
                self.maze[x[0] + z[0] + 1][x[1] + z[1] + 1] = 'C'
        self.maze[0][1] = 'C'
        self.maze[-1][-2] = 'C'

    def get_maze(self):
        return self.maze
