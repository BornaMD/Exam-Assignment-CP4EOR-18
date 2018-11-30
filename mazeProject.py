class Maze:
    def __init__(self,filename):
        #Reads input file:
        fh=open(filename,"r")
        line=fh.readlines()
        fh.close()
                
        #Create 2D array called maze:
        maze=[]
        rowcount=0
        for x in line:
            l=x.strip()
            rowcount+=1
            array=[]
            colcount=0
            for y in l:
                array.append(int(y))
                colcount+=1
            maze.append(array)
        #print(maze)
        #print(rowcount,colcount)
        self.maze=maze
        
        #Create attribute finish which contains a list of 2 integers:
        for r in range(rowcount):
            if maze[r][0]==0:
                self.finish=[r,0]
            elif maze[r][-1]==0:
                self.finish=[r,colcount-1]
            continue
        for c in range(colcount):
            if maze[0][c]==0:
                self.finish=[0,c]
            elif maze[-1][c]==0:
                self.finish=[rowcount-1,c]
            continue
        #print(self.finish)    
        #Create object of class Robot which takes the input as starting position:
        for r in range(rowcount):
            for c in range(colcount):
                if maze[r][c]==2:
                    self.start=[r,c]
                    #print(self.start)
        self.robot=Robot(self.start)
       
    #Create a method which returns the location of the finish of the maze:
    def get_finish(self):
        return self.finish
    
    #Create method which returns the list containing the maze:
    def get_grid(self):
        return self.maze
    
    #Create method which returns a 3x3 list containing all the adjacent tiles to pos:
    def get_neighbourhood(self,pos):
        hood=[[],[],[]]
        for r in range(-1,2):
            for c in range(-1,2):
                hood[c+1] += [self.maze[pos[0]+c][pos[1]+r]]
        return hood
        
class Robot(Maze):
    def __init__(self,currentPos):
        self.currentPos=currentPos
        self.lastPos= self.currentPos
        self.Maze=Maze()
        self.lastDirection=""

    #Create a method to change the last position of the robot into the current position and change the current position into the position indicated by the input of the method.
    def change_pos(self,pos):
        self.lastPos=self.currentPos
        self.currentPos=pos
    
    #Create a method which which returns a list containing the coordinates of the current position of the robot:
    def get_pos(self):
        return self.currentPos
    
    #Create a method which returns dictionary of options:
    def walk_options(self):
        #def walk_options(self):
        options={}
        hood=self.Maze.get_neighbourhood(self.currentPos)
        pos=self.get_pos()
        r=pos[0]
        c=pos[1]
        if hood[0][1] == "0":
            options["up"] = [y-1,x] 
        if hood[2][1] == "0":
            options["down"] = [y+1,x]
        if hood[1][2] == "0":
            options["right"] = [y,x+1]    
        if hood[1][0] == "0":
            options["left"] = [y,x-1]
        return options

    #Create a method which will change the last direction of the Robot:
    #def change_direction
    def change_direction(self):
        count=0
        for i in self.walk_options():
            if self.lastDirection==i:#check if the current last direction is in the possibilities
                count=1
        if count==1:
            self.walk_options.pop(self.lastDirection,None)#removing the current last direction out of the dictorial list
            #We change its direction below
            #I have it set to randomly choose a different direction
            #but you can change the line below if ya like
        self.lastDirection=random.choice(list(self.walk_options())) 
        return self.lastDirection #return a new direction
    
    #Create a method which returns boolean if the robot is at the finish:
    def is_finished(self):
        if self.currentPos==self.get_finish():
            return True
        else:
            return False

    #Create navigation algorithm
    def take_one_step(robot):    
       if self.lastDirection!="up" or self.lastDirection!="down" or self.lastDirection!="right" or self.lastDirection!="left": 
            self.change_direction()#if the last direction is still not defined yet such as an open string then we choose a direction
        self.change_pos(walk_options().options[self.lastDirection])
        #change the position by the dictorial list containing lastdirection
        #for example change pos requires a list of 2 integers. Suppose your last direction is "up" then find the coordinates of "up"
        #this is my intention with walk_options() method and its attribute options[lastDirection]
        #still have to add changing direction if you hit a wall with the current direction (example LastDirection is up and up is a wall)
        



def main():
    maze1=Maze('maze1.txt')
    print(maze1.get_neighbourhood([1,2]))
    print(maze1.robot.walk_options())
    #maze2 = Maze('maze2.txt')
    #robot1=maze1.robot
    #robot2=maze2.robot
main()
