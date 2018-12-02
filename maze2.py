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
                neighbourhood[j+1] += [self.maze[pos[0]+j][pos[1]+i]]
        return neighbourhood
        

class Robot:
    def __init__(self,classmaze, start):
        self.currentpos = start
        self.lastpos = self.currentpos
        self.maze = classmaze
        self.lastdir = 0 #start with direction "right"
        self.rightcount = 0
        self.leftcount = 0
        self.rightcount2 = 0
        self.leftcount2 = 0
    
    # Methods
    def change_pos(self, pos):
        self.lastpos = self.currentpos
        self.currentpos = pos

    def get_pos(self):
        return self.currentpos

    def walk_options(self):
        hood = self.maze.get_neighbourhood(self.currentpos)

        options = {}
        row = self.currentpos[0]
        column = self.currentpos[1]

        if hood[1][2] != 1: #because we also want to walk on 2
            options[0] = [row,column+1]
            options[360] = [row,column+1]

        if hood[0][1] != 1:
            options[90] = [row-1,column]
        
        if hood[1][0] != 1:
            options[180] = [row,column-1]
        
        if hood[2][1] != 1:
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
        
        while self.currentpos != self.maze.get_finish(): #so it doesn't continue when the while loop of the main is not done with other mazes, would give index error
            
            options = self.walk_options()

                # setting turning counts to zero after right and left hand wallfollower were stuck in circle
            if (self.rightcount>=5 or self.leftcount>=5) and (self.rightcount2>=5 or self.leftcount2>=5):
                self.rightcount, self.leftcount, self.rightcount2, self.leftcount2 = 0,0,0,0
            
            elif self.rightcount <5 and self.leftcount<5:

                if self.lastdir == 0: #to make if statements work with angles
                    self.change_lastdir(360)

                # right hand to the wall
                if (self.lastdir-90) in options:
                    self.change_pos(options[self.lastdir-90])
                    self.change_lastdir(self.lastdir-90)
                    self.rightcount += 1
                    self.leftcount = 0
                elif self.lastdir in options:
                    self.change_pos(options[self.lastdir])
                else:
                    if self.lastdir == 360:
                        self.change_lastdir(0)

                    if (self.lastdir+90) in options:
                        self.change_pos(options[90+self.lastdir])
                        self.change_lastdir(90 + self.lastdir)
                        self.leftcount += 1
                        self.rightcount = 0
                    else:
                        self.change_pos(self.lastpos)
                        if self.lastdir ==90:
                            self.change_lastdir(270)
                        else:
                            self.change_lastdir(abs(180-self.lastdir))
            else:
                # left hand to wall

                if self.lastdir == 360:
                        self.change_lastdir(0)

                if (self.lastdir+90) in options:
                        self.change_pos(options[90+self.lastdir])
                        self.change_lastdir(90 + self.lastdir)
                        self.leftcount2 += 1
                        self.rightcount2 = 0

                elif self.lastdir in options:
                    self.change_pos(options[self.lastdir])
                else:
                    if self.lastdir ==0:
                        self.change_lastdir(360)

                    if (self.lastdir-90) in options:
                        self.change_pos(options[self.lastdir-90])
                        self.change_lastdir(self.lastdir-90)
                        self.rightcount2 += 1
                        self.leftcount2 = 0
                    
                    else:
                        self.change_pos(self.lastpos)
                        if self.lastdir ==90:
                            self.change_lastdir(270)
                        else:
                            self.change_lastdir(abs(180-self.lastdir))

            return self.currentpos

        


def main():

    maze1 = Maze("testcase1.txt") 
    maze2 = Maze("testcase2.txt") 
    robot1 = maze1.robot 
    robot2 = maze2.robot 
    path1 =[]
    path2 =[]

    i = 0
    while i<100 and (robot1.is_finished() == False or robot2.is_finished() == False): 
        path1.append(robot1.take_one_step())
        path2.append(robot2.take_one_step())
        i +=1

    print(path1)
    print(path2)

main()

# To-do's:
# change main to have different while loops, or if possible get none out of solution
# nicer code, right and left hand wall follower similar code, just order switched up

# Q's:
# okay if direction is in terms of angles not "up", "down", etc.?
# rows and column outputs in real rows and columns or python way of numbering?
# does it have to find the optimal way or just the way out?