class dead_end_fill:
    def __init__(self)
        fh = open("maze1.txt", "r")
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
        fh.close()
        self.row = 0
        self.column = 0
        self.width = len(maze_array[1])
        self.height = len(maze_array)
        for i in range(self.height):
            for j in range(self.width):
                   back_track(i,j)
                   
    #save function which I wanted to add later on
    # def __save(self):
    #     fo=open("maze1.txt","w")
    #     for i in range(self.width): 

    
    def is_dead_end(self,x,y):
        #my idea is that you gain the row and column (x,y)
        #you then check if at least 3 positions are 1. If that is the case then its a dead end.
        count=0
        #if your current position is a 1 then by default it can't be a dead end
        if maze_array[x][y]==1:
            return False
        #Checks if the location is the finish, which can never be a dead end
        if x==0 or x==(len(maze_array)-1) or y==0 or y==(len(maze_array[0])-1):
                return False
        #Check all the adjecent vertices
        else:
                if maze_array[x-1][y]==1:       
                        count+=1
                if maze_array[x+1][y]==1:
                        count+=1        
                if maze_array[x][y-1]==1:
                        count+=1
                if maze_array[x][y+1]==1:
                        count+=1
        if count==3:
            return True
        else:
            return False

               
    #I added this method, because suppose you only have 1 dead end left. It goes from the dead end to the finish line. 
    #In between the dead end and finish line is your starting point. Hence, you require this method such that the dead end stops at your starting point
    #See test case 1 and try to do it with hand!
    def is_starting_pos(self,x,y):
        if maze_array[x][y]==2: #If the starting location is the dead end you don't want to use the algorithm down below either
            return True
        else:
            return False

    def back_track(self,x,y):
        #Step 1: check if its a dead end and not a starting area. If this condition holds, turn the coordinate into a 1
        if is_dead_end(x,y)==True and is_starting_pos(x,y)==False: #See description at is_adjecent_starting_pos
                maze_array[x][y]=1
                    #Step 2: Look for the adjecent vertex that is 0. This location is now a dead end (unless you arrive at a junction)
                    #Step 3: Using recursion we turn that coordinate into a 1
                if  maze_array[x-1][y]==0:  #By default we know there can only be a single 0 in any of these since this is checked in "is_dead_end(x,y)==True:", hence I do not need to put any constraints
                    return back_track(x-1,y)
                if maze_array[x+1][y]==0:
                    return back_track(x+1,y)
                if maze_array[x][y-1]==0:
                    return back_track(x,y-1)
                if maze_array[x][y+1]==0:
                    return back_track(x,y+1)
        #Step 4: This continues until there is no dead end left. If its no longer a dead end, stop the algorithm.
        else:
            # save() #I was intending to add a save function that writes all of this on a new file for clarity. This would also be the new file that the robot walks on.
            return maze_array
            #Note if it reaches the starting position then it will also be seen as a junction. In the end there should be only 1 path left that leads from starting point, 2, to the goal

            #My take on the algorithm class. I noticed you copied nearly everything from internet. This is fine, however it makes understanding it a bit more complex. I personally used very common methods to write it. 
#Its not complete yet though. There are a few issues left:
BIG NOTE: USE THE OTHER TESTING FILE. THE ALGORITHM WORKS!!!!! HOWEVER IT CAN STILL BE REFINED. LOOK DOWN BELOW 
#1) SOLVED
#2) I was intending to write a save function so that the new array can be used for the robot. The new array will only have an optimal path left.
#3) I have yet to test the later part of my code. Hence, I am 1000% certain that it will require some debugging.
#4) I opened the mase1.txt file, but its better to drag the maze from the maze class instead. Basically its like merging things together so that it moves fluently.
