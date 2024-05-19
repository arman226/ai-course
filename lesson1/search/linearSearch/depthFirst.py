import sys

sys.path.append("lesson1/search/linearSearch") 
from implem.StackFrontier import StackFrontier
from utils.MazeSolver import MazeSolver


def search():  
    if len(sys.argv) != 2:
        print("Usage: python depthFirstSearch.py maze.txt <stack|queue>")
        return

    maze_file = sys.argv[1]
    solver= MazeSolver(maze_file,StackFrontier)
    solver.solve()

search()
