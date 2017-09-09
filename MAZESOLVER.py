'''Program to find the way in maze'''
  
BLOCK = "#"
MOVE = "-"
 
def solve_maze(maze, size):
     ''' To solve the maze. It internally includes two other functions'''
     solution = []
     for i in range(size):
         for j in range(size):
             solution.append(BLOCK) 
     solution = [solution[i:i + size] for i in range(size)]
     if check(maze, 0, 0, solution, size) == False:
         print("Solution doesn't exist")
         return False
     if maze[size - 1][size - 1] == BLOCK:
         print("Solution doesn't exist")
         return False
     print_Solution(solution, size)      
     return True
               
def check(maze, x, y, solution, size):
    ''' Trace out the way by backtracking method'''
    if x == size - 1  and y == size - 1:
         solution[x][y] = MOVE
         return True
    if is_safe(maze, x, y, size):
         solution[x][y] = MOVE
         if check(maze, x + 1, y, solution, size):
             return True
         if check(maze, x, y + 1, solution, size):
             return True
         solution[x][y] = BLOCK
         return False
    return False

def print_Solution(solution, size):
    '''Prints the way that is solved matrix. 
    It takes the solution matrix as a parameter'''
    for i in range(size):
         for j in range(size):
             print(solution[i][j], end = " ")
         print()

def is_safe(maze, x, y, size):
    '''Checks whether the path in which we are is safe that is it is
    not a block'''
    return size > x >= 0 and size > y >= 0 and maze[x][y] == "-"
          
name = input("Enter the file name:")
mazefile = open(name,"r")
maze = []
for line in mazefile:
     maze.append(line.strip().split())
mazefile.close()
size = len(maze)  
solve_maze(maze, size) 

