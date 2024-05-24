import sys
from heapq import heappop, heappush

# Add the path to the module containing HeuristicMazeSolver
sys.path.append("lesson1/search/linearSearch")
from implem.PriorityQueueFrontier import PriorityQueueFrontier
from utils.HeuristicMazeSolver import HeuristicMazeSolver as MazeSolver


# A* Maze Solver class extending the HeuristicMazeSolver class
class AStarMazeSolver(MazeSolver):
    def __init__(self, file_name):
        # Initialize the base class with the maze file and the frontier class
        super().__init__(file_name, PriorityQueueFrontier)
        # Set the heuristic function to Manhattan distance
        self.heuristic = self.manhattan_distance

    def search(self):
        # Add the starting position to the frontier with initial cost 0
        self.frontier.add((self.start, [self.start], 0), self.heuristic(self.start))
        explored = set()

        # Continue searching until there are nodes in the frontier
        while not self.frontier.is_empty():
            # Remove the node with the highest priority (lowest cost + heuristic)
            current_pos = self.frontier.remove()
            current, path, cost = current_pos

            # Skip if the node has already been explored
            if current in explored:
                continue

            explored.add(current)
            self.visited[current[0]][current[1]] = True

            # Check if the current node is the end position
            if self.maze[current[0]][current[1]] == "E":
                self.path = path
                return True

            # Explore neighboring nodes
            for move_x, move_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x, next_y = current[0] + move_x, current[1] + move_y
                if self.is_valid_move(next_x, next_y) and (next_x, next_y) not in explored:
                    next_node = (next_x, next_y)
                    new_cost = cost + 1
                    priority = new_cost + self.heuristic(next_node)
                    self.frontier.add((next_node, path + tuple([next_node]), new_cost), priority)

        return False
