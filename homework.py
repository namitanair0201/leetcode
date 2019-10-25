# -*- coding: utf-8 -*-
import heapq
from collections import deque
from math import sqrt

def heuristic(cell, target):
    return int(sqrt((cell[0]-target[0])**2 + (cell[1]-target[1])**2))

def trace_pathUCSAstar(parent_child_dict, goal, start):
    """
    (dict, str, str) -> list

    parent_child_dict: dictionary - contains child as key and parent as value
    goal: string, contains xy coords of goal node
    start: string, contains xy coords of start node
    """
    #initialize path to goal node
    path = [goal]
    #traverse till we reach start node
    while(path[-1] != start):
        previous = str(parent_child_dict[path[-1]][1])
        path.append(previous)
    path.reverse()
    return path

def getCost(frontier, new_neighbor):
    """ (list of tuples, list) -> returns int
    """
    for item in frontier:
        if item[1]== new_neighbor:
            return item[0]


def getNeighborAstar(grid, parent, R, C, max_z, target, current_priority=0):
    # direction vectors
    dr = [-1,-1,-1,0,1,1, 1, 0]
    dc = [-1, 0, 1,1,1,0,-1,-1]
    neighbors = []

    for i in range(8):
        #Y-AXIS
        test_row = parent[0] + dr[i]
        #X-AXIS
        test_col = parent[1] + dc[i]

        #skip invalid cells
        if test_col<0 or test_row<0 or test_row>= C or test_col>= R:
            continue
        
        #####Proceed only if the cell is not visited before
            
        z_diff = abs(grid[test_col][test_row] - grid[parent[1]][parent[0]])
        
        if z_diff <= max_z:

            #If the test cell is not a diagonal we add 10 else 14
            if dr[i]==0 or dc[i]==0:
                cost = 10 
            else:
                cost = 14

            cost += current_priority + z_diff + heuristic([test_row,test_col], target) - heuristic(parent, target)
            neighbors.append( (cost, [test_row,test_col]) )
    return neighbors    

def AStarSearch(grid, landing, target, max_z, R, C):

    path = "FAIL"
    
    #1. initializing all the data structures and adding the start node to the heap
    frontier = []
    explored = []
    parent_child_dict = {}

    frontier.append((0, landing)) 
    parent_child_dict[str(landing)] = (0,landing)
    
    while(frontier):    
        
        #2. node ← POP(frontier ) /* chooses the lowest-cost node in frontier */
        parent_priority, parent = heapq.heappop(frontier)
        
        frontier_coords = [x[1] for x in frontier]

        
        # 3. if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
        if parent == target:
            path = trace_pathUCSAstar(parent_child_dict, str(target), str(landing))
            break

        # 4. add node.STATE to explored
        explored.append(parent)


        # 5. for each action in problem.ACTIONS(node.STATE) do
        temp = getNeighborAstar(grid, parent, R, C, max_z, target, parent_priority)
        neighbor_costs = [x[0] for x in temp if x[1] not in explored ]
        new_neighbors = [x[1] for x in temp if x[1] not in explored]
        
        for cost, new_neighbor in zip(neighbor_costs,new_neighbors):
            
            if new_neighbor in frontier_coords:
                
                frontier_cost = getCost(frontier, new_neighbor) 
                if cost < frontier_cost:
                    frontier.remove((frontier_cost,new_neighbor))
                    frontier.append((cost,new_neighbor))
                    parent_child_dict[str(new_neighbor)]= (cost,parent)  
                    
            else:    
                parent_child_dict[str(new_neighbor)] = (cost,parent)  
                frontier.append((cost,new_neighbor))       
    
    return path


def getNeighborUCS(grid, parent, R, C, max_z, current_priority=0):
    
    # direction vectors
    dr = [-1,-1,-1,0,1,1, 1, 0]
    dc = [-1, 0, 1,1,1,0,-1,-1]
    neighbors = []

    for i in range(8):
        #Y-AXIS
        test_row = parent[0] + dr[i]
        #X-AXIS
        test_col = parent[1] + dc[i]

        #skip invalid cells
        if test_col<0 or test_row<0 or test_row>= C or test_col>= R:
            continue
        
        #####Proceed only if the cell is not visited before
            
        z_difference = abs(grid[test_col][test_row] - grid[parent[1]][parent[0]])
        
        if z_difference <= max_z:

            #If the test cell is not a diagonal we add 10 else 14
            cost = 10 if (dr[i]==0 or dc[i]==0) else 14

            neighbors.append( (current_priority+cost, [test_row,test_col]) )

    return neighbors    

def UniformCostSearch(grid, landing, target, max_z, R, C):

    path = "FAIL"
    
    #1. initializing all the data structures and adding the start node to the heap
    frontier = []
    explored = []
    parent_child_dict = {}

    frontier.append((0, landing)) 
    parent_child_dict[str(landing)] = (0,landing)
    
    while(frontier):    
        
        parent_priority, parent = heapq.heappop(frontier)
        frontier_coords = [x[1] for x in frontier]

        
        if parent == target:
            path = trace_pathUCSAstar(parent_child_dict, str(target), str(landing))
            break

        explored.append(parent)

        temp = getNeighborUCS(grid, parent, R, C, max_z, parent_priority)
        neighbor_costs = [x[0] for x in temp if x[1] not in explored ]
        new_neighbors = [x[1] for x in temp if x[1] not in explored]
        
        for cost, new_neighbor in zip(neighbor_costs,new_neighbors):
            if new_neighbor in frontier_coords:
                frontier_cost = getCost(frontier, new_neighbor) 
                if cost < frontier_cost:
                    frontier.remove((frontier_cost,new_neighbor))
                    frontier.append((cost,new_neighbor))
                    parent_child_dict[str(new_neighbor)]= (cost,parent)  
                    
            else:    
                parent_child_dict[str(new_neighbor)]= (cost,parent)  
                frontier.append((cost,new_neighbor))       
    
    return path


def tracePathBFS(path, target, landing):
    """
    (dict, str, str) -> str
    """
    result = [target]
    while(landing != result[-1]):
        prev = str(path[result[-1]])
        result.append(prev)
    result.reverse()
    return result

def getNeighborBFS(grid,landing, R, C, max_z):

    """
    (list, int, int) -> list of lists

    landing: [list of x,y current cell]
    R,C: total rows and cols
    takes the current cell coords as input and
    returns a list of neighbor cell coords as output

        0               1           2
    0   (x-1,y-1)|    (x-1,y)|  (x-1,y+1)
    1   (x,y-1)  |    (x,y)  |  (x,y+1)
    2   (x+1,y-1)|    (x+1,y)|  (x+1,y+1)
    we start comparing cells from 00 and move clockwise
    when we talk about row and col we mean row and col of matrix and not the x,y coords
    
    """

    # direction vectors
    dr = [-1,-1,-1,0,1,1,1,0]
    dc = [-1,0,1,1,1,0,-1,-1]
    neighbors = []
    
    #getting the index of the possible neighbors
    for i in range(8):
        test_row = landing[1] + dr[i]
        test_col = landing[0] + dc[i]
        #skip invalid cells
        if test_col<0 or test_row<0 or test_row>= R or test_col>= C :
            continue

        #check for z
        if abs(grid[test_row][test_col] - grid[landing[1]][landing[0]]) <= max_z:
            neighbors.append([test_col,test_row])
        
        #we append the test_col, test_row as we want to store x,y coords
    return neighbors

def BreadthFirstSearch(grid, landing, target, max_z, R, C):
    """ 
        (2D matrix(int), list, list, int, int, int) -> Str

        grid : 2D matrix
        R,C : no of nodes and cols
        landing : start node coords
        target : goal node coords
        
        data structures used:
        frontier : stores the nodes that are to be explored, FIFO queue
        visited : stores the nodes that have already been visisted
        parent_child_dict : tracing path---> dict[child] = parent

        functions called:
        getNeighborCells(landing, R, C): finding neighbors
        trace_path(parent_child_dict, ): returns the shortest path
    """

    visited = []
    parent_child_dict = {}
    frontier = deque()
    path = "FAIL"
    parent_child_dict[str(landing)] = landing
    # 1. Add starting node to frontier, also add the parent child relationship to the dictionary
    frontier.append(landing)
    
    #repeat while there are nodes to be explored
    while( frontier ):
        
        # 3. Pop first node from the queue
        current_cell = frontier.popleft()
    
        #4. Check if target found
        if current_cell==target:
            path = tracePathBFS(parent_child_dict, str(target), str(landing))
            break
        
        # 5. Check if node has already been visited.
        if current_cell not in visited:
            
            # 6. If not, go through the neighbours of the node.
            neighbors = getNeighborBFS(grid, current_cell,R,C, max_z)    

            # 7. Add the neighbour nodes to the queue.
            for neighbor in [cell for cell in neighbors if cell not in visited ]:
                frontier.append(neighbor)  
                parent_child_dict[str(neighbor)] = current_cell 
                    
            # 8. Mark the node as explored.
            visited.append(current_cell)

    return path


def startRun(grid, landing, targets, max_z, R, C):
    """
    (2d matrix(int), list, list of lists, int, int, int) -> None

    grid: 2D matrix
    landing: start node
    targets: the list of targets to be found
    max_z: the max z elevatiom
    R: the total no of rows
    C: the total no of cols

    """

    path = ""
    
    if search_type=='A*':
        for target in targets:
            if landing!=target:
                result = AStarSearch(grid, landing, target, max_z, R, C)
            else:
                result = str(landing).strip('[').strip(']').replace(' ','')
            
            if landing == target or result=='FAIL':
                path += result+ '\n'
            else:
                path += ' '.join(x_y.replace(' ','') for x_y in result)+'\n'

    elif search_type == 'BFS':
        for target in targets:
            if landing!=target:
                result = BreadthFirstSearch(grid, landing, target, max_z, R, C)
            else:
                result = str(landing).strip('[').strip(']').replace(' ','')
            
            if landing == target or result=='FAIL':
                path += result+ '\n'
            else:
                path += ' '.join(x_y.replace(' ','') for x_y in result)+'\n'
    
    elif search_type=='UCS':
        for target in targets:
            if landing!=target:
                result = UniformCostSearch(grid, landing, target, max_z, R, C)
            else:
                result = str(landing).strip('[').strip(']').replace(' ','')
            
            if landing == target or result=='FAIL':
                path += result + '\n'
            else:
                path += ' '.join(x_y.replace(' ','') for x_y in result)+'\n'

    
    path = ''.join(char_ for char_ in path if char_ not in "'[]")
    path = path.strip()
    f = open("output.txt", 'w')
    f.write(path)
    f.close()

if __name__ == "__main__":
    #read the file and assign all variables 
    f = open("input.txt", 'r')

    search_type = f.readline().rstrip('\n')

    C,R = map(int, f.readline().strip().split())

    landing = list(map(int, f.readline().strip().split()))
    
    max_z = int(f.readline())

    n_target = int(f.readline())
    targets = []
    for i in range(n_target):
        targets.append(list(map(int, f.readline().split())))
    
    grid = [list(map(int, f.readline().split()))  for y in range(R)]
    f.close()
    #reading finished now start with assigning the correct function for the same
    startRun(grid, landing, targets, max_z, R, C)