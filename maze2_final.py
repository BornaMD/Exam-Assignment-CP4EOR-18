class Maze:

    def __init__(self, filename):
        fh = open(filename, "r")

        # Maze matrix
        maze = []

        for line in fh:
            line = line.strip()
            newline = []
            for element in line:
                element = int(element)
                newline.append(element)
            if newline != [] :
                maze.append(newline)    
        self.maze = maze

        #Find finish point
        finish = []

        for element in maze[0]:
            if element == 0:
                finish.append(0)
                finish.append(maze[0].index(element))

        for element in maze[-1]:
            if element == 0:
                finish.append(len(maze)-1)
                finish.append(maze[-1].index(element))
        
        for line in maze:
            if line[0] == 0:
                finish.append(maze.index(line))
                finish.append(0)
        
        for line in maze:
            if line[-1] == 0:
                finish.append(maze.index(line))
                finish.append(len(line)-1)

        self.finish = finish

        # Find starting point
        start = []
        for line in maze:
            for element in line:
                if element == 2:
                    start.append(maze.index(line))
                    start.append(line.index(element))
        self.start = start

        # Robot
        self.robot = Robot(self, self.start)

    # Methods   
    def get_finish(self):
        return self.finish

    def get_grid(self):
        return self.maze
    
    def get_neighbourhood(self,pos):
        neighbourhood = [[],[],[]]
        for i in range(-1,2):
            for j in range(-1,2):
                neighbourhood[i+1].append(self.maze[pos[0]+i][pos[1]+j])
        return neighbourhood
        

class Robot:
    def __init__(self,classmaze, start):
        self.currentpos = start
        self.lastpos = start
        self.maze = classmaze
        self.lastdir = 0 #start with direction "right"
        self.anglecount = 0 #adding up total angles
        self.sign = 1 #positive sign: right hand wall follower, negative sign: left hand wall follwer
        self.oneleftturn = 0 #checking if lefthand wall follower made one turn to left
        
    
    # Methods
    def change_pos(self, pos):
        self.lastpos = self.currentpos
        self.currentpos = pos

    def get_pos(self):
        return self.currentpos

    def walk_options(self):
        nhood = self.maze.get_neighbourhood(self.currentpos)

        options = {}
        row = self.currentpos[0]
        column = self.currentpos[1]

        # we are using angles of the unit circle instead of directions. Therefore, direction East is angle 0 and 360. direction North is 90 degrees, etc.

        if nhood[1][2] != 1: #because we also want to walk on 2
            options[0] = [row,column+1]
            options[360] = [row,column+1]

        if nhood[0][1] != 1:
            options[90] = [row-1,column]
        
        if nhood[1][0] != 1:
            options[180] = [row,column-1]
        
        if nhood[2][1] != 1:
            options[270] = [row+1,column]

        return options
    
    def change_lastdir(self, direction):
        self.lastdir = direction
    
    def is_finished(self):
        if self.currentpos == self.maze.get_finish():
            return True
        else:
            return False
    
    def take_one_step(self):

        if self.is_finished() == False: 
            options = self.walk_options()
                # the robot follows the wall with his right hand, if he encounters a circle, hence turning 360 degrees in total, he will switch to being a left hand follower until he makes a left turn

                # setting turning counts, one-turn to zero after either right in circle (turned for a total of 360 degrees), or if left hand wall follower made one turn, and changing sign (so left to right or right to left)
            if self.anglecount==360 or self.oneleftturn == 1:
                self.anglecount = 0
                self.sign *= (-1) # sign = 1 represents right hand wall follower, sign = -1 represents left hand wall follower.
                self.oneleftturn = 0 

            
            # This helps to work with 0 and 360 degrees being the same direction but both represented in the code
            if self.sign == 1:
                if self.lastdir == 0: 
                    self.change_lastdir(360)
            else:
                if self.lastdir == 360: 
                    self.change_lastdir(0)

            # first try to turn right if sign = 1, turn left if sign = -1, if possible
            if (self.lastdir-90*self.sign) in options:
                self.change_pos(options[self.lastdir-90*self.sign])    
                self.change_lastdir(self.lastdir-90*self.sign)
                self.anglecount= self.anglecount + 90 # no need to consider left hand turn, because anglecount will be set to zero after this step
                self.oneleftturn = (-1)*self.sign # setting one turn to 1 if left hand wall follower, to fulfil condition above

            # try to go straight
            elif self.lastdir in options:
                self.change_pos(options[self.lastdir])
            else:
                #changing 360 and 0 degrees again to work with following code
                if self.sign ==1:
                    if self.lastdir == 360:
                        self.change_lastdir(0)
                else:                        
                    if self.lastdir == 0: 
                        self.change_lastdir(360)

                # try to turn left if sign = 1, turn right if sign = -1
                if (self.lastdir+90*self.sign) in options:
                    self.change_pos(options[90*self.sign+self.lastdir])
                    self.change_lastdir(90*self.sign + self.lastdir)
                    self.anglecount = self.anglecount - 90 #no need to consider left hand because if he got stuck in "right"circle there must be a escape on the left at some point

                # else go back to your last position
                else:
                    self.change_pos(self.lastpos)
                    if self.lastdir ==90:
                        self.change_lastdir(270)
                    else:
                        self.change_lastdir(abs(180-self.lastdir))
                    self.anglecount = self.anglecount - 180 # a dead end is like 2 left turns in the corners

            return self.currentpos
        else:
            return self.currentpos
            
def main():

    maze1 = Maze("testcase5.txt") 
    maze2 = Maze("testcase6.txt") 
    maze3 = Maze("testcase7.txt")
    robot1 = maze1.robot 
    robot2 = maze2.robot 
    robot3 = maze3.robot
    path1 =[]
    path2 =[]
    path3 =[]
    
    i = 0
    while i<100 and (robot1.is_finished() == False or robot2.is_finished() == False or robot3.is_finished() == False): 
        path1.append(robot1.take_one_step())
        path2.append(robot2.take_one_step())
        path3.append(robot3.take_one_step())
        i +=1

    print(path1)
    print(path2)
    print(path3)

main()

# Q's:
# okay if direction is in terms of angles not "up", "down", etc.? ok as long as explained
# rows and column outputs in real rows and columns or python way of numbering? python numbering
# does it have to find the optimal way or just the way out? no, but guaranteed way out
# okay to return the final postion many times? yes, more elegant than none, maybe change output
# get_grid, actual grid or just matrix? just matrix
