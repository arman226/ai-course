class MazeSolver:
    def __init__(self, file_name, frontier):
        self.maze=self.read_maze(file_name) #see implementation below
        self.start=self.find_start()
        self.end=self.find_end()
        self.visited =[[False for _ in row] for row in self.maze]  #initially set all item in vistited as false
        self.path=[]
        self.frontier = frontier()

    # file reader function
    def read_maze(self, file_name):
        with open(file_name, 'r') as f:
            # converting each line into a list of characters, and storing these lists within another list representing rows of the maze. 
            maze = [list(line.strip()) for line in f]
        return maze 
    
    def find_start(self):
        for i, row in enumerate(self.maze):
            for j,val in enumerate(row):
                if val=="S":
                    return i,j
        return None
    
    def find_end(self):
        for i, row in enumerate(self.maze):
            for j,val in enumerate(row):
                if val=="E":
                    return i,j
        return None  
    
    def is_valid_move(self, x, y):
        # if the coordinates are not valid, return False
        if x<0 or x>len(self.maze) or y<0 or y>len(self.maze[0]):
            return False
        # if the coordinates point to a wall "#" or if the coordinates are alraedy tagged as visited, return False
        if self.maze[x][y] == "#" or self.visited[x][y]:
            return False
        return True
    
    def search(self):
        self.frontier.add((self.start, [self.start]))
        explored = set() #start with empty explored set

        while self.frontier:
            (current,path) = self.frontier.remove()
            
            if current in explored: 
                continue #if the current pointer points to a node that is explored already, skip the current iteration and move to the next 

            #add the current node to the explored set and to the visited set
            explored.add(current)
            self.visited[current[0]][current[1]] = True

            if self.maze[current[0]][current[1]] =="E": #goal test
                self.path = path
                return True
            
            for move_x, move_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #navigating all possible moves
              next_x, next_y = current[0] + move_x, current[1] + move_y
              if self.is_valid_move(next_x, next_y) and (next_x, next_y) not in explored:
                  self.frontier.add(((next_x, next_y), path + [(next_x, next_y)]))

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
            # self.print_explored_paths()
            return True
        else:
            print("No path found from start to end.")
            return False