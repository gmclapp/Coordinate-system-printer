class obstacle():
    def __init__(self, location, radius, height):
        self.loc = location
        self.r = radius
        self.h = height

    def collision_detect(self, point):
        '''This function accepts a column vector and checks if it collides with
        the obstacle object.'''
        d = (self.loc[:,:]-point[:,:])**2
        + (self.loc[:,:]-point[:,:])**2
        + (self.loc[:,:]-point[:,:])**2

        if d <= self.r:
            return(True)
        else:
            return(False)

class node():
    def __init__(self, location):
        self.loc = location

    def set_walkable(self, walk=True):
        '''If walk is True, the node is reachable, and is not blocked by an
        obstacle.'''
        self.walk = walk

def generate_obstacle(obstacle, o_list):
    '''Initialize an obstacle and append it to the list of obstacles.'''
    o_list.append(obstacle(obstacle))
    return(o_list)

def generate_path(start, goal, *obstacles):
    '''This function generates a path given a starting location, a goal
    location, and an arbitrary number of obstacles.'''
    o_list = []
    for o in obstacles:
        o_list = generate_obstacle(o, o_list)

def initialize_grid():
    grid = np.empty((i,j,k), dtype=object)
    for x in range(i):
        for y in range(j):
            for z in range(k):
                grid[i,j,k] = node(point(i,j,k))
                # where point is a column vector object
                
        
    
