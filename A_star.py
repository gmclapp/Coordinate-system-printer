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
        self.closed = False
        self.opened = False

    def open_node(self, gcost, hcost, parent=None):
        if parent != None:
            #print("This node has a parent!")
            self.parent_g_cost = parent.gcost
        else:
            #print("This node has no parent node. It's g-cost is zero")
            self.parent_g_cost = 0

        self.gcost = self.parent_g_cost + gcost
        self.hcost = hcost
        self.fcost = self.gcost + self.hcost
        
    def print_node(self):
        print("X: ",self.loc.x,
              "Y: ",self.loc.y,
              "Z: ",self.loc.z,
              "\nG-cost: ",self.gcost,
              "\nH-cost: ",self.hcost,
              "\nF-cost: ",self.fcost,sep='')
    def set_walkable(self, walk=True):
        '''If walk is True, the node is reachable, and is not blocked by an
        obstacle.'''
        self.walk = walk

    def open_me(self):
        self.opened = True
    def close_me(self):
        self.closed = True

class work_envelope():
    def __init__(self, x_dim, y_dim, z_dim, dx=1, dy=1, dz=1):
        
        self.grid = []

    def dist(self,n1, n2):
        d = (((n1.loc.x-n2.loc.x)*self.dx)**2
             + ((n1.loc.y-n2.loc.y)*self.dy)**2
             + ((n1.loc.z-n2.loc.z)*self.dz)**2)**0.5

        return(d)

    def check_match(self, n1, n2):
        if n1.loc == n2.loc:
            match = True
        else:
            match = False
            
    def close_node(self, n, end):
        # temporary variables for current node
        x = n.loc.x
        y = n.loc.y
        z = n.loc.z

        opened_nodes=[]
        #Explore x dimension
        gcost = self.dx
        if x-1 >= 0:
            hcost = self.dist(self.grid[x-1][y][z], end)
            self.grid[x-1][y][z].open_node(gcost, hcost, n)
            opened_nodes.append(self.grid[x-1][y][z])
        if x+1 < self.x_dim:
            hcost = self.dist(self.grid[x+1][y][z], end)
            self.grid[x+1][y][z].open_node(gcost, hcost, n)
            opened_nodes.append(self.grid[x+1][y][z])
            

        #Explore y dimension
        gcost = self.dy
        if y-1 >= 0:
            hcost = self.dist(self.grid[x][y-1][z], end)
            self.grid[x][y-1][z].open_node(gcost, hcost, n)
            opened_nodes.append(self.grid[x][y-1][z])
        if y+1 < self.y_dim:
            hcost = self.dist(self.grid[x][y+1][z], end)
            self.grid[x][y+1][z].open_node(gcost, hcost, n)
            opened_nodes.append(self.grid[x][y+1][z])

        #Explore z dimension
        gcost = self.dz
        if z-1 >= 0:
            hcost = self.dist(self.grid[x][y][z-1], end)
            self.grid[x][y][z-1].open_node(gcost, hcost, n)
            opened_nodes.append(self.grid[x][y][z-1])
        if z+1 < self.z_dim:
            hcost = self.dist(self.grid[x][y][z+1], end)
            self.grid[x][y][z+1].open_node(gcost, hcost, n)
            opened_nodes.append(self.grid[x][y][z+1])

        #Explore side diagonals
        gcost = (self.dy**2 + self.dx**2)**0.5
        if x-1>=0:
            if y-1>=0:
                hcost = self.dist(self.grid[x-1][y-1][z], end)
                self.grid[x-1][y-1][z].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x-1][y-1][z])
            if y+1 < self.y_dim:
                hcost = self.dist(self.grid[x-1][y+1][z], end)
                self.grid[x-1][y+1][z].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x-1][y+1][z])
        if x+1 < self.x_dim:
            if y-1>=0:
                hcost = self.dist(self.grid[x+1][y-1][z], end)
                self.grid[x+1][y-1][z].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x+1][y-1][z])
            if y+1 < self.y_dim:
                hcost = self.dist(self.grid[x+1][y+1][z], end)
                self.grid[x+1][y+1][z].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x+1][y+1][z])
        
        gcost = (self.dx**2+self.dz**2)**0.5
        if x-1 >=0:
            if z-1>=0:
                hcost = self.dist(self.grid[x-1][y][z-1], end)
                self.grid[x-1][y][z-1].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x-1][y][z-1])
            if z+1<self.z_dim:
                hcost = self.dist(self.grid[x-1][y][z+1], end)
                self.grid[x-1][y][z+1].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x-1][y][z+1])
        if x+1<self.x_dim:
            if z-1>=0:
                hcost = self.dist(self.grid[x+1][y][z-1], end)
                self.grid[x+1][y][z-1].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x+1][y][z-1])
            if z+1<self.z_dim:
                hcost = self.dist(self.grid[x+1][y][z+1], end)
                self.grid[x+1][y][z+1].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x+1][y][z+1])
        
        gcost = (self.dy**2+self.dz**2)**0.5
        if y-1>=0:
            if z-1>=0:
                hcost = self.dist(self.grid[x][y-1][z-1], end)
                self.grid[x][y-1][z-1].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x][y-1][z-1])
            if z+1<self.z_dim:
                hcost = self.dist(self.grid[x][y-1][z+1], end)
                self.grid[x][y-1][z+1].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x][y-1][z+1])
        if y+1<self.y_dim:
            if z-1>=0:
                hcost = self.dist(self.grid[x][y+1][z-1], end)
                self.grid[x][y+1][z-1].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x][y+1][z-1])
            if z+1<self.z_dim:
                hcost = self.dist(self.grid[x][y+1][z+1], end)
                self.grid[x][y+1][z+1].open_node(gcost, hcost, n)
                opened_nodes.append(self.grid[x][y+1][z+1])

        #Explore corners
        gcost = (self.dx**2+self.dy**2+self.dz**2)**0.5
        if x+1<self.x_dim:
            if y+1<self.y_dim:
                if z+1<self.z_dim:
                    hcost = self.dist(self.grid[x+1][y+1][z+1], end)
                    self.grid[x+1][y+1][z+1].open_node(gcost, hcost, n)
                    opened_nodes.append(self.grid[x+1][y+1][z+1])
                if z-1>=0:
                    hcost = self.dist(self.grid[x+1][y+1][z-1], end)
                    self.grid[x+1][y+1][z-1].open_node(gcost, hcost, n)
                    opened_nodes.append(self.grid[x+1][y+1][z-1])
            if y-1>=0:
                if z+1<self.z_dim:
                    hcost = self.dist(self.grid[x+1][y-1][z+1], end)
                    self.grid[x+1][y-1][z+1].open_node(gcost, hcost, n)
                    opened_nodes.append(self.grid[x+1][y-1][z+1])
                if z-1>=0:
                    hcost = self.dist(self.grid[x+1][y-1][z-1], end)
                    self.grid[x+1][y-1][z-1].open_node(gcost, hcost, n)
                    opened_nodes.append(self.grid[x+1][y-1][z-1])
        if x-1>=0:
            if y+1<self.y_dim:
                if z+1<self.z_dim:
                    hcost = self.dist(self.grid[x-1][y+1][z+1], end)
                    self.grid[x-1][y+1][z+1].open_node(gcost, hcost, n)
                    opened_nodes.append(self.grid[x-1][y+1][z+1])
                if z-1>=0:
                    hcost = self.dist(self.grid[x-1][y+1][z-1], end)
                    self.grid[x-1][y+1][z-1].open_node(gcost, hcost, n)
                    opened_nodes.append(self.grid[x-1][y+1][z-1])
            if y-1>=0:
                if z+1<self.z_dim:
                    hcost = self.dist(self.grid[x-1][y-1][z+1], end)
                    self.grid[x-1][y-1][z+1].open_node(gcost, hcost, n)
                    opened_nodes.append(self.grid[x-1][y-1][z+1])
                if z-1>=0:
                    hcost = self.dist(self.grid[x-1][y-1][z-1], end)
                    self.grid[x-1][y-1][z-1].open_node(gcost, hcost, n)
                    opened_nodes.append(self.grid[x-1][y-1][z-1])
        n.close_me()
        return(opened_nodes)

def generate_obstacle(obstacle, o_list):
    '''Initialize an obstacle and append it to the list of obstacles.'''
    o_list.append(obstacle)
    return(o_list)

def generate_path(start, goal, *obstacles):
    '''This function generates a path given a starting location, a goal
    location, and an arbitrary number of obstacles.'''

    epsilon = 0.25
    w_env = work_envelope(3, 3, 4)
    
    path_complete = False
    
    o_list = []
    
    for o in obstacles:
        o_list = generate_obstacle(o, o_list)

    start_node = start
    goal_node = goal
    start_h_cost = w_env.dist(start_node, goal_node)

    start_node.open_node(0, start_h_cost, parent=None)
    
    open_nodes = [] # nodes to be evaluated
    newly_open = w_env.close_node(start_node, goal_node)
    
    for n in newly_open:
        open_nodes.append(n)
        n.print_node()

    print("\n\n\n")    
    closed_nodes = [start_node] # nodes that have already been evaluated
    
    while path_complete == False:
        open_nodes.sort(key=lambda x: x.fcost, reverse=False)
        current=open_nodes.pop(0)
        newly_open = w_env.close_node(current, goal_node)
        for n in newly_open:
            if n.closed == False and n.opened == False:
                n.open_me()
                open_nodes.append(n)
                
            if n.hcost < epsilon:
                path_complete=True
        for n in open_nodes:
            n.print_node()
        closed_nodes.append(current)
            
            
    


        
    
                
        
    
