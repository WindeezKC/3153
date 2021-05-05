# The grid values must be separated by spaces, e.g.
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# Returns a 2D list of 1s and 0s
import queue
import random

class Node:
     def __init__(self,value,par):
        self.value=value 
        self.par = par 



   
    


def uninformedSearch(grid,start,goal):
    
    print('In uninformed Search')
    current = Node(start,'')
    openList=queue.Queue()
    closedList=[]


    #while True:
       # if openList.empty()==current:
        

            
            

    
    
def getNeighbors(location,grid):
    for i in range(1,grid):
        if(location[i][0]] != 0):
            location[i][0] = location [i-1][0]
    for i in range (1,grid):
        if(location[i+1][0] != 0):
            location[i][0]=location[i+1][0]
    for i in range(1,grid):
        if(location[0][j+1]):
            location[0][j]=location[0][j+1]

    for j in range (1, grid):
        if (location[0][j] != 0):
            location[0][j] = location[0][j-1]

    for i in range(1,grid):
        for j in range(1,grid):
            if(location[i][j] != 0):
                location[i][j] = max(location[i][j-1],location[i-1][j])

  
#if location[0] > 0:
        #upperNeighbor=[location[0]-1,location[1]]
      #  if grid[upperNeighbor[0],[upperNeighbor[1]] == 0:
       #     results.append(upperNeighbor)

   # if location[1] < len(grid[0]):
    #    rightNeighbor = [location[0],location[1]+1]
    #    if grid[rightNeighbor[0],rightNeighbor[1]]==0:
     #       results.append(rightNeighbor)
        
   # if location[1]>len(grid[1]):
    #    lowerRightNeighbor=[location[0]+1,location[1]]
    #    if grid[lowerRightNeighbor[0],lowerRightNeighbor[1]]==0:
    #        results.append(lowerRighNeighbor)
   # if location[1] >0:
   #     leftNeighbor=[location[0],location[1]-1]
    #    if grid[leftNeighbor[0],leftNeighbor[1]] ==0:
     #       results.append(leftNeighbor)
    #
   # return grid.append(results[])

   



    #Main Task: breaking out of while loop
def readGrid(filename):
    #print('In readGrid')
    grid = []
    with open(filename) as f:
        for l in f.readlines():
            grid.append([int(x) for x in l.split()])
   
    f.close()
    #print 'Exiting readGrid'
    return grid
 
 
# Writes a 2D list of 1s and 0s with spaces in between each character
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
def outputGrid(grid, start, goal, path):
    #print('In outputGrid')
    filenameStr = 'path.txt'
 
    # Open filename
    f = open(filenameStr, 'w')
 
    # Mark the start and goal points
    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'
 
    # Mark intermediate points with *
    for i, p in enumerate(path):
        if i > 0 and i < len(path)-1:
            grid[p[0]][p[1]] = '*'
 
    # Write the grid to a file
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
           
            # Don't add a ' ' at the end of a line
            if c < len(row)-1:
                f.write(str(col)+' ')
            else:
                f.write(str(col))
 
        # Don't add a '\n' after the last line
        if r < len(grid)-1:
            f.write("\n")
 
    # Close file
    f.close()
    #print('Exiting outputGrid')
    readGrid('Grid.txt')
    print(getNeighbors(readGrid))