from random import randint


class Maze:
    def __init__(self, dimensions):
        self.maze = list(list('W' for x in range(2 * dimensions[0] + 1)) for y in range(
            2 * dimensions[1] + 1))  # first marks everything as a wall
        for x in range(len(self.maze)):
            for y in range(len(self.maze[0])):
                if y % 2 == 1 and x % 2 == 1:
                    self.maze[x][y] = 'R'   # odd spaces are rooms
                if y == 0 or y == len(self.maze[0]) - 1 or x == 0 or x == len(self.maze) - 1:
                    self.maze[x][y] = 'W'

        self.visited = list(list(0 for x in range(dimensions[0])) for y in range(
            dimensions[1]))    # visited matrix keeps track of which rooms have been visited
        self.dimensions = dimensions

        self.adjacency = dict()  # keeps track of which rooms are linked to each other
        for x in range(dimensions[1]):
            for y in range(dimensions[0]):
                self.adjacency[(x, y)] = list()

    def traverse(self, node):
        """Runs DFS to run complete search through all rooms"""
        self.visited[node[0] // 2][node[1] // 2] = 1
        open = list()
        for x, y in [(0, 1), (-1, 0), (0, -1), (1, 0)]:  # for all the adjacent rooms
            if 0 <= node[0] + 2 * x < len(self.maze) and 0 <= node[1] + 2 * y < len(self.maze[0]):
                # if the room hasn't been visted yet
                if self.visited[(node[0] + 2 * x) // 2][(node[1] + 2 * y) // 2] == 0:
                    # adds the room as traversable
                    open.append((node[0] + 2 * x, node[1] + 2 * y))
                    # sets the room as visited
                    self.visited[(node[0] + 2 * x) //
                                 2][(node[1] + 2 * y) // 2] = 1

        j = list(print(x) for x in self.visited)
        while len(open) > 0:    # takes a random room within the traversables and traverses it
            next_v = open.pop(randint(0, len(open) - 1))
            print(node, next_v, self.dimensions,
                  (len(self.maze), len(self.maze[0])))
            # adds room to current room's list
            self.adjacency[(node[0] // 2, node[1] // 2)
                           ].append((next_v[0] // 2, next_v[1] // 2))
            # adds current room to room's list
            self.adjacency[(next_v[0] // 2, next_v[1] // 2)
                           ].append((node[0] // 2, node[1] // 2))
            self.traverse(next_v)

    def fill(self):
        """Runs the recursive traverse method; allows after recursion calls"""
        self.traverse((1, 1))
        for x, y in self.adjacency.items():
            for z in y:
                # sets all the corridors as actual corridors reflected on the maze
                self.maze[x[0] + z[0] + 1][x[1] + z[1] + 1] = 'C'
        self.maze[0][1] = 'C'
        self.maze[-1][-2] = 'C'

        j = list(print(x) for x in self.maze)

    def get_maze(self):
        return self.maze


Maze((13, 14)).fill()
