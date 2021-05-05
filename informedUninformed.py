import math
import random
import queue

start=[1,1]
goal=[4,4]
path = ''






def uninformedSearch(grid, start, goal):
	print('In uninfoirmed Search')
	current = start
	openList=queue.Queue()
	
	closedList=[start]


	while True:
		print(current)
		moves = getNeighbors(current,grid)
		print(moves)
		if goal in moves:
			return closedList

		current = setPath(current, moves, grid)
		closedList.append(current)

if not openList.empty() or current == goal:

        # Set the path variable
    setPath(current, path)

        # Append the goal because setPath doesn't add that
    path.append(goal)

return [path, numExpanded]

	








def getNeighbors(location,grid):
    neb=[]
	
	# up
    if location[0] != 0:
        if grid[location[0]-1][location[1]] != 0:
            neb.append([location[0]-1,location[1]]) 
	# down
    if location[0] <= len(grid)-1:
        if grid[location[0]+1][location[1]] != 0:
            neb.append([location[0]+1,location[1]]) 
	# left
    if location[1] !=0:
        if grid[location[0] ][location[1]-1] != 0:
            neb.append([location[0],location[1]-1]) 
	# right 
    if location[1] < len(grid[0]) -1:
        if grid[location[0]][location[1]+1] != 0:
            neb.append([location[0],location[1]+1]) 

	
    return neb


def setPath(current,path, grid):

	return path[random.randint(0,len(path)-1)]







# The grid values must be separated by spaces, e.g.
# 1 1 1 1 1 
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1
# Returns a 2D list of 1s and 0s
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
	filenameStr = 'path2.txt'

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
	#print('Exiting outputGrid')n

grid = readGrid('Grid2.txt')
print(grid)
path = uninformedSearch(grid, start, goal)
outputGrid(grid, start, goal, path)
