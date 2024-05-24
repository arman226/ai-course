import sys

sys.path.append("lesson1/search/linearSearch") 
from utils.AStarMazeSolver import AStarMazeSolver


def search():
    if len(sys.argv) != 2:
        print("Usage: python astar.py maze.txt")
        return

    maze_file = sys.argv[1]
    solver = AStarMazeSolver(maze_file)
    solver.solve()

search()