class Maze:
    def __init__(self, file):
        # Open the file:
        fh = open(str(file), "r")
        content = fh.readlines()
        # maze_array is a two-dimensional array with the entire maze (integers):
        maze_array = []
        # Fill maze_array with numbers from file:
        for i in range(len(content)):
            line = str(content[i]).strip()
            linelist = []
            for element in line:
                linelist.append(int(element))
            maze_array.append(linelist)
        self.maze_array = maze_array
        # Find finish of maze, i.e. zero on the side:
        # Coordinates of this finish line. Start at (0, 0):
        row = 0
        column = 0
        width = len(maze_array[1])
        height = len(maze_array)
        success = 0
        # Check the upper and lower rows:
        for i in range(width):
            if maze_array[0][column] == 0:
                success = 1
                break
            if maze_array[height-1][column] == 0:
                success = 1
                row = height-1
                break
            else:
                column += 1
        # Check left and right sides (lowest en highest positions were already checked, so it starts at 1 and ends at height-1):
        if success == 0:
            row = 1
            column = 0
            for k in range(1,height-1):
                if maze_array[row][0] == 0:
                    success = 1
                    break
                if maze_array[row][width-1] == 0:
                    success = 1
                    column = width-1
                    break
                else:
                    row += 1
        # Save finish coordinate as attribute:
        self.finish = [row, column]
        # Finding the starting position
        starting_pos=[]
        for i in range(height):
            for j in range(width):
                if maze_array[i][j]==2:
                    starting_pos.append([i,j])
        # Create an object of the class robot with the starting position
        test=Robot(starting_pos)
    # Method that returns the location of the finish
    def get_finish(self):
        return self.finish
    # Method that returns the list containing the maze
    def get_grid(self):
        return self.maze_array
    # Method that returns a 3x3 list containing all tiles adjacent to pos
    def get_neighbourhood(self,pos):
        threebythree = [[],[],[]]
        for i in range(-1,2):
            for j in range(-1,2):
                threebythree[j+1] += [self.maze_array[pos[0]+j][pos[1]+i]]
        return threebythree
