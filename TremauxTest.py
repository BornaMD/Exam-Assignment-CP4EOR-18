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
row = 0
column = 0
width = len(maze_array[1])
height = len(maze_array)
starting_pos=[]
for i in range(height):
        for j in range(width):
                if maze_array[i][j]==2:
                        starting_pos.append(i)
                        starting_pos.append(j)
# print(maze_array)

def is_dead_end(x,y,i):
        count=0
        if maze_array[x][y]==1:
                return False
        if x==0 or x==(len(maze_array)-1) or y==0 or y==(len(maze_array[0])-1):
                return False
        elif maze_array[x][y]==i and (maze_array[x+1][y]==0 or maze_array[x-1][y]==0 or maze_array[x][y-1]==0 or maze_array[x][y+1]==0):
                return False
        else:
                if maze_array[x-1][y]!=0 and maze_array[x-1][y]!=i:       
                        count+=1
                if maze_array[x+1][y]!=0 and maze_array[x+1][y]!=i:
                        count+=1        
                if maze_array[x][y-1]!=0 and maze_array[x][y-1]!=i:
                        count+=1
                if maze_array[x][y+1]!=0 and maze_array[x][y+1]!=i:
                        count+=1
        if count==3:
                return True
        else:
                return False

def is_junction(x,y):
    count=0
    if maze_array[x][y]==1:
        return False
    if x==0 or x==(len(maze_array)-1) or y==0 or y==(len(maze_array[0])-1):
        return False
    else:
        if maze_array[x-1][y]==0:       
                count+=1
        if maze_array[x+1][y]==0:
                count+=1        
        if maze_array[x][y-1]==0:
                count+=1
        if maze_array[x][y+1]==0:
                count+=1
    if count>=2:
        return True
    else:
        return False

def Finish(x,y,u,v):
        if x==u and y==v:
                return True
        else:
                return False

def back_track(x,y,u,v,i):
    maze_array[x][y]="X"
    if maze_array[x-1][y]==i:
        return back_track(x-1,y,u,v,i)
    elif maze_array[x+1][y]==i:
        return back_track(x+1,y,u,v,i)
    elif maze_array[x][y-1]==i:
        return back_track(x,y-1,u,v,i)
    elif maze_array[x][y+1]==i:
        return back_track(x,y+1,u,v,i)
    else:
        maze_array[x][y]=i-1
        return walking(x,y,u,v,i-1) #turn this off and run each stap manually and it will work
        # return maze_array,x,y #turn this on and run each step manually and it will work
        
        
        # Still trying to figure out where the mistakes is

def walking(x,y,u,v,i):
        if is_junction(x,y)==False and is_dead_end(x,y,i)==False and Finish(x,y,u,v)==False:
                maze_array[x][y]=i 
                if maze_array[x-1][y]==0:       
                        return walking(x-1,y,u,v,i)
                if maze_array[x+1][y]==0:
                        return walking(x+1,y,u,v,i)      
                if maze_array[x][y-1]==0:
                        return walking(x,y-1,u,v,i)
                if maze_array[x][y+1]==0:
                        return walking(x,y+1,u,v,i) 
        elif is_junction(x,y)==True:
                maze_array[x][y]=i+1
                if maze_array[x-1][y]==0:       
                        return walking(x-1,y,u,v,i+1)
                if maze_array[x+1][y]==0:
                        return walking(x+1,y,u,v,i+1)        
                if maze_array[x][y-1]==0:
                        return walking(x,y-1,u,v,i+1)
                if maze_array[x][y+1]==0:
                        return walking(x,y+1,u,v,i+1)
        elif is_dead_end(x,y,i)==True:
                return back_track(x,y,u,v,i)
        elif Finish(x,y,u,v)==True:
                maze_array[x][y]=i 
                return maze_array
        
x=starting_pos[0]
y=starting_pos[1]
u=6
v=10
i=2
walking(x,y,u,v,i)
# print() 
# print(maze_array)#Turn all these below on and make sure the upper items are on/off then turn it on and it will work
# print(is_dead_end(5,1,3))
# walking(5,1,6,10,3)
# print()
# print(maze_array)
# print(is_junction(5,4))
# walking(5,4,6,10,3)
# print()
# print(maze_array)
# walking(5,4,6,10,3)
# print()
# print(maze_array)
# walking(3,1,6,10,2)
# print()
# print(maze_array)
# c1=walking(1,2,6,10,2)
# print()
# print(maze_array)
# # walking(4,9,6,10,2)
# # print()
# # print(maze_array)
# print(x)
# print(y)
print(maze_array)

