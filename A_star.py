import sanitize_inputs as si

class obstacle():
    def __init__(self, location, radius, height=float('Inf')):
        self.loc = location
        self.r = radius
        self.h = height

    def collision_detect(self, point):
        '''This function accepts a column vector and checks if it collides with
        the obstacle object.'''
        d = (self.loc.x-point.loc.x)**2 # This will not run, just outlining.
        + (self.loc.y-point.loc.y)**2
        + (self.loc.z-point.loc.z)**2

        if (self.loc.z <= point.loc.z <= self.loc.z + self.h) and d <= self.r:
            return(True)
        else:
            return(False)

class node():
    def __init__(self, location):
        self.loc = location

    def open_node(self, parent=None):
        if parent != None:
            self.parent_g_cost = parent.gcost
        else:
            self.parent_g_cost = 0
        
        # calculate h-cost
        # calculate f-cost
        # add to open list
    
    def set_walkable(self, walk=True):
        '''If walk is True, the node is reachable, and is not blocked by an
        obstacle.'''
        self.walk = walk

    def set_gcost(self, cost):
        self.g_cost = self.parent_g_cost + cost

    def set_hcost(self, cost):
        # how far away from the end node
        self.h_cost = cost

    def set_fcost(self):
        self.f_cost = self.g_cost+self.h_cost

def dist(n1, n2):
    d = ((n1.loc.x-n2.loc.x)**2
         + (n1.loc.y-n2.loc.y)**2
         + (n1.loc.z-n2.loc.z)**2)**0.5

    return(d)

def generate_obstacle(obstacle, o_list):
    '''Initialize an obstacle and append it to the list of obstacles.'''
    o_list.append(obstacle)
    return(o_list)

def generate_path(start, goal, *obstacles):
    '''This function generates a path given a starting location, a goal
    location, and an arbitrary number of obstacles.'''

    path_complete = False
    
    o_list = []
    start_node = node(start)
    goal_node = node(goal)

    start_node.open_node()
    start_node.set_gcost(0)
    start_node.set_hcost(dist(start, goal))
    start_node.set_fcost()
                         
    open_nodes = [node(start)] # nodes to be evaluated
    closed_nodes = [] # nodes that have already been evaluated
    
    for o in obstacles:
        o_list = generate_obstacle(o, o_list)

    while path_complete == False:
        for n in open_nodes:
            # find node with the lowest fcost and open its neighbors.
            # close n
            pass
            

def initialize_grid(x_dim, y_dim, z_dim):

    grid = []
    for k in range(z_dim):
        column = []
        for j in range(y_dim):
            row = []
            for i in range(x_dim):
                print("Adding node: (",i,',',j,',',k,')',sep='')
                row.append(node(si.col_vec([i,j,k])))
            column.append(row)
        grid.append(column)

    return(grid)


        
    
                
        
    
