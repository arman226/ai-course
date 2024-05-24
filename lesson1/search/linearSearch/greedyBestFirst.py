import sys

sys.path.append("lesson1/search/linearSearch") 
from implem.PriorityQueueFrontier import PriorityQueueFrontier
from utils.HeuristicMazeSolver import HeuristicMazeSolver as MazeSolver


def search():
    if len(sys.argv) != 2:
        print("Usage: python greedyBestFirst.py maze.txt")
        return

    maze_file = sys.argv[1]
    solver = MazeSolver(maze_file, PriorityQueueFrontier)
    solver.solve()


search()