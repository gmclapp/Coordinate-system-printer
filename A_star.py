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

    def open_node(self, gcost, hcost, parent=None):
        if parent != None:
            print("This node has a parent!")
            self.parent_g_cost = parent.gcost
        else:
            print("This node has no parent node. It's g-cost is zero")
            self.parent_g_cost = 0

        self.gcost = self.parent_g_cost + gcost
        self.hcost = hcost
        
    def print_node(self):
        print("X: ",self.loc.x,
              "Y: ",self.loc.y,
              "Z: ",self.loc.z,
              "\nG-cost: ",self.gcost,sep='')
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

class work_envelope():
    def __init__(self, x_dim, y_dim, z_dim, dx=1, dy=1, dz=1):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        
        self.grid = []
        for k in range(z_dim):
            column = []
            for j in range(y_dim):
                row = []
                for i in range(x_dim):
                    print("Adding node: (",i,',',j,',',k,')',sep='')
                    row.append(node(si.col_vec([i*dx,j*dy,k*dz])))
                column.append(row)
            self.grid.append(column)

    def dist(self,n1, n2):
        d = ((n1.loc.x-n2.loc.x)**2
             + (n1.loc.y-n2.loc.y)**2
             + (n1.loc.z-n2.loc.z)**2)**0.5

        return(d)

    def close_node(self, n):
        # temporary variables for current node
        x = self.grid[n.loc.x][n.loc.y][n.loc.z].loc.x
        y = self.grid[n.loc.x][n.loc.y][n.loc.z].loc.y
        z = self.grid[n.loc.x][n.loc.y][n.loc.z].loc.z

        opened_nodes=[]
        #Explore x dimension
        gcost = self.dx
        hcost = 0 # replace this with a distance calculation to the end node
        self.grid[x-1][y][z].open_node(gcost, hcost, n)
        self.grid[x+1][y][z].open_node(gcost, hcost, n)

        #Explore y dimension
        gcost = self.dy
        hcost = 0 # replace this with a distance calculation to the end node
        self.grid[x][y-1][z].open_node(gcost, hcost, n)
        self.grid[x][y+1][z].open_node(gcost, hcost, n)

        #Explore z dimension
        gcost = self.dz
        hcost = 0 # replace this with a distance calculation to the end node
        self.grid[x][y][z-1].open_node(gcost, hcost, n)
        self.grid[x][y][z+1].open_node(gcost, hcost, n)

        #Explore side diagonals
        gcost = (self.dy**2 + self.dx**2)**0.5
        hcost = 0 # replace this with a distance calculation to the end node
        self.grid[x-1][y-1][z].open_node(gcost, hcost, n)
        self.grid[x-1][y+1][z].open_node(gcost, hcost, n)
        self.grid[x+1][y-1][z].open_node(gcost, hcost, n)
        self.grid[x+1][y+1][z].open_node(gcost, hcost, n)
        gcost = (self.dx**2+self.dz**2)**0.5
        self.grid[x-1][y][z-1].open_node(gcost, hcost, n)
        self.grid[x-1][y][z+1].open_node(gcost, hcost, n)
        self.grid[x+1][y][z-1].open_node(gcost, hcost, n)
        self.grid[x+1][y][z+1].open_node(gcost, hcost, n)

        
        
        self.grid[x-1][y][z].print_node()
        print("Node (",x,",",y,",",z,")")

def generate_obstacle(obstacle, o_list):
    '''Initialize an obstacle and append it to the list of obstacles.'''
    o_list.append(obstacle)
    return(o_list)

def generate_path(start, goal, *obstacles):
    '''This function generates a path given a starting location, a goal
    location, and an arbitrary number of obstacles.'''

    w_env = work_envelope(2, 3, 4)
    
    path_complete = False
    
    o_list = []
    
    for o in obstacles:
        o_list = generate_obstacle(o, o_list)

    start_node = start
    goal_node = goal
    start_h_cost = w_env.dist(start_node, goal_node)

    start_node.open_node(0, start_h_cost, parent=None)
    start_node.print_node()
    
    open_nodes = [] # nodes to be evaluated
    w_env.close_node(start_node)
                         
    closed_nodes = [start_node] # nodes that have already been evaluated
    
    while path_complete == False:
        for n in open_nodes:
            # find node with the lowest fcost and open its neighbors.
            # close n
            pass
            
    


        
    
                
        
    
