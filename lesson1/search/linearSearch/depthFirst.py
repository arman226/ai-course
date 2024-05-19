import sys

from linearSearch.implem import StackFrontier
from linearSearch.utils import MazeSolver


def search():  
    if len(sys.argv) != 3:
        print("Usage: python depthFirstSearch.py maze.txt <stack|queue>")
        return

    maze_file = sys.argv[1]
    solver= MazeSolver(maze_file,StackFrontier)
    solver.solve()
