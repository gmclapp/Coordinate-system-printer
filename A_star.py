class obstacle():
    def __init__(self, location, radius, height):
        self.loc = location
        self.r = radius
        self.h = height

    def collision_detect(self, point):
        '''This function accepts a column vector and checks if it collides with
        the obstacle object.'''
        d = (self.loc.x-point.loc.x)**2 # This will not run, just outlining.
        + (self.loc.y-point.loc.y)**2
        + (self.loc.z-point.loc.z)**2

        if d <= self.r:
            return(True)
        else:
            return(False)

class node():
    def __init__(self, location):
        self.loc = location

    def open_node(self, parent):
        # copy path from parent
        pass
    
    def set_walkable(self, walk=True):
        '''If walk is True, the node is reachable, and is not blocked by an
        obstacle.'''
        self.walk = walk

    def set_gcost(self, start_loc):
        # how far away from the start node
        pass

    def set_hcost(self, end_loc):
        # how far away from the end node
        pass

    def set_fcost(self):
        # gcost + hcost
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
    o_list = []
    open_nodes = [node(start)] # nodes to be evaluated
    closed_nodes = [] # nodes that have already been evaluated
    
    for o in obstacles:
        o_list = generate_obstacle(o, o_list)

def initialize_grid():
    grid = np.empty((i,j,k), dtype=object)
    for x in range(i):
        for y in range(j):
            for z in range(k):
                grid[i,j,k] = node(point(i,j,k))
                # where point is a column vector object
                
        
    
