class HeuristicMazeSolver:
    def __init__(self, file_name, frontier):
        self.maze = self.read_maze(file_name)
        # Finds the starting point (marked as 'S') in the maze and stores its coordinates
        self.start = self.find_start()
        # Finds the ending point (marked as 'E') in the maze and stores its coordinates
        self.end = self.find_end()
        self.visited = [[False for _ in row] for row in self.maze] #Initializes a 2D list self.visited to keep track of visited cells in the maze. All cells are initially set to False.
        self.path = [] #Initializes an empty list self.path to store the path from the start to the end if found.
        self.frontier = frontier() #Initializes the frontier (a data structure managing nodes to be explored) by calling the provided frontier function.
        self.heuristic = self.manhattan_distance
        
# in this case, the maze becomes a 2 dimensional array
    def read_maze(self, file_name):
        with open(file_name, 'r') as f:
            maze = [list(line.strip()) for line in f]   
        return maze

    def find_start(self): 
         # Iterate through each row of the maze using enumerate to get both index and row content
        for i, row in enumerate(self.maze):
            # Iterate through each value in the row using enumerate to get both index and value
            for j, val in enumerate(row):
                if val == "S": 
                    return i,j    
        return None
 
    def find_end(self):
         # Iterate through each row of the maze using enumerate to get both index and row content
        for i, row in enumerate(self.maze):
            # Iterate through each value in the row using enumerate to get both index and value
            for j, val in enumerate(row):
                if val == "E":
                    return i, j
        return None
    #Checks if a move to position (x, y) is valid. i.e self.maze[x][y]
    def is_valid_move(self, x, y):
        if x < 0 or x >= len(self.maze) or y < 0 or y >= len(self.maze[0]):
            return False
        # Ensures the position is within maze bounds, not a wall ('#'), and not already visited.
        if self.maze[x][y] == "#" or self.visited[x][y]:
            return False
        return True
    
    def manhattan_distance(self, node):
        (x1, y1) = node
        (x2, y2) = self.end
        return abs(x1 - x2) + abs(y1 - y2)

    def search(self):
        # Adds the start node to the frontier with its heuristic value.
        self.frontier.add((self.start, [self.start]), self.heuristic(self.start))
        explored = set()#Initializes an empty set explored to keep track of explored nodes.
        # Continuously explores nodes from the frontier until it's empty:
        while not self.frontier.is_empty():
            current_pos = self.frontier.remove() #Removes a node from the frontier.
            current, path = current_pos

            if current in explored:
                continue #Skips the node if already explored.

            explored.add(current) #Marks the node as explored and visited.
            self.visited[current[0]][current[1]] = True

            if self.maze[current[0]][current[1]] == "E": #Checks if the current node is the end; if so, stores the path and returns True.
                self.path = path
                return True
            #Generates valid neighboring nodes and adds them to the frontier with their heuristic values.
            for move_x, move_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x, next_y = current[0] + move_x, current[1] + move_y
                if self.is_valid_move(next_x, next_y) and (next_x, next_y) not in explored:
                    next_node = (next_x, next_y)
                    self.frontier.add((next_node, path + tuple([next_node])), self.heuristic(next_node))

        return False

    def print_maze_with_path(self):
        maze_copy = [row[:] for row in self.maze]
        for x, y in self.path:
            if maze_copy[x][y] not in ('S', 'E'):
                maze_copy[x][y] = '*'
        for row in maze_copy:
            print(''.join(row))

    def print_explored_paths(self):
        maze_copy = [row[:] for row in self.maze]
        for x in range(len(self.visited)):
            for y in range(len(self.visited[0])):
                if self.visited[x][y]:
                    if (x, y) not in self.path:
                        maze_copy[x][y] = 'X'
                    elif maze_copy[x][y] not in ('S', 'E'):
                        maze_copy[x][y] = '*'
        for row in maze_copy:
            print(''.join(row))

    def solve(self):
        if not self.start:
            print("Start position 'S' not found in the maze.")
            return False

        if not self.end:
            print("End position 'E' not found in the maze.")
            return False

        if self.search():
            print("Path found:")
            self.print_maze_with_path()
            return True
        else:
            print("No path found from start to end.")
            return False
