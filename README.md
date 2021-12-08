# Lab08

Lab 08: Game Time! (Search and Sort on Graphs)
Due: Thursday, December 16, 2021, before class  (2+ Python modules and 1 Google doc)

Instructions:
You and a partner will collaborate to write two classic game programs and brainstorm a graph-based solution to another game.  It is up to you to divide the work, but I strongly urge you to evenly distribute the design and coding.  No matter what, both partners are expected to understand the solutions well enough to explain them.
Some of these programs are GUI-based so you should use Zelle’s graphics library (introduced last year in Computer Science and (H) Computer Science).  If you need this library, you can find the file and install instructions on our course page under Topics > Reference Material.  You can also download the Graphics API there.
At the top of every module and document, please include both partners’ names and a brief description of how the labor was divided for that exercise.  
Both partners should submit all files for this lab in a folder called Lab08.
During class on Thursday, Dec 16, you will group-grade each others’ labs and fill out a partner evaluation (worth 3 points).  Both of these will be combined with my evaluation for your final lab score.

Exercises:
(8 pt) Minesweeper is a single-player game where the goal is to try to find all mines hidden in a N x M grid. You can read the full set of rules here (and play a couple of games as well!).  

For this program, you and your partner will recreate parts of this game using a GUI.  Your implementation should include the following:
An 8 x 8 board with 10 randomly placed mines
When the user clicks on a cell, the program should either (1) reveal the new clue(s) or (2) show the detonated bomb and end the game.
If the user clicks on a cell with no bombs as its neighbors, your program should use BFS to reveal all necessary clue cells.  
When the game ends (either because the user clicked on a bomb or the only unrevealed cells are bombs), the user should have the option of replaying.
Button to replay and a button to quit
You are welcome to include any other aspects of the original game but they are not required for full credit.

It is up to you and your partner to decide how you want to implement this game, but I request that any classes be written in separate modules and that the main program be written in a module called Lab08Minesweeper.py. 

(8 pts) For this program, you’ll use DFS to create a maze using a GUI.  The user should enter the dimensions of the maze (with a maximum area of 1000 cells) and a randomly generated maze of that size should be displayed on the graphics window.  You can decide how you want to indicate the start and end but the start of the maze should be the top left corner and the end should be the bottom right.   Your program does NOT need to include a way for the user to traverse the maze but should have the ability to generate a new maze or quit when the user is ready.

To create an N x M maze, you should use a 2-dimensional array with dimensions (2N + 1) x (2M + 1). The outer boundary of the array (rows 0 and 2N and columns 0 and 2M) is composed entirely of walls. We'll call cells where both indices are odd our 'room' cells and all other cells 'corridor' cells.  To generate your maze, DFS should operate in the following fashion for each room cell (i, j):
Mark the room (i, j) as 'visited'
Randomly order the neighboring rooms to apply DFS.  For each neighbor:
If the neighbor was not visited, then mark the corridor between the cells as walkable and recurse on the neighbor.
If the neighbor was visited and the corridor was not yet marked, mark the corridor as a wall.
Note that we're using DFS to randomly generate a walkable path, but then drawing walls to prevent any cycles from forming.  Please save this program in a module called Lab08Maze.py.

(6 pts) Pick-up Sticks is a game where sticks are tossed into a pile on the floor. Players then alternate turns trying to pick up one stick at a time without disturbing any others. If they move more than one stick, then their turn ends. The player with the most sticks wins the game. For more details, go to https://en.wikipedia.org/wiki/Pick-up_sticks.

Without consulting the internet beyond the link above, give a graph formulation for the game such that topological sort tells you the winning order to remove sticks (assuming you have the dexterity to do it!).  After describing your graph, show how it works on the example game below.  Specifically, draw out the corresponding graph, topologically sort the vertices, and explain how it’s a valid winning strategy.



Write your response to this exercise in a Google Doc called Lab08PickUpSticks and include both of your names at the top of the document.

