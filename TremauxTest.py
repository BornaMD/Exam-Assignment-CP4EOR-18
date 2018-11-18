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

def is_dead_end(x,y,i):
    count=0
    if maze_array[x][y]==1:
        return False
    if x==0 or x==(len(maze_array)-1) or y==0 or y==(len(maze_array[0])-1):
            return False
    else:
            if maze_array[x-1][y]!=0 or maze_array[x-1][y]!=i:       
                    count+=1
            if maze_array[x+1][y]!=0 or maze_array[x+1][y]!=i:
                    count+=1        
            if maze_array[x][y-1]!=0 or maze_array[x][y-1]!=i:
                    count+=1
            if maze_array[x][y+1]!=0 or maze_array[x][y+1]!=i:
                    count+=1
    if count>=3:
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

def back_track(x,y,i):
    maze_array[x][y]=1
    if maze_array[x-1][y]==i:
        return back_track(x-1,y,i)
    elif maze_array[x+1][y]==i:
        return back_track(x+1,y,i)
    elif maze_array[x][y-1]==i:
        return back_track[x][y-1]
    elif maze_array[x][y+1]==i:
        return back_track[x][y+1]
    else:
        return back_track[x][y]

def walking(x,y,i):
    
