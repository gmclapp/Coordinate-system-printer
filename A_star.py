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
        self.parent = parent
        if parent != None:
            self.parent_g_cost = parent.gcost
        else:
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

class work_envelope():
    def __init__(self, x_dim, y_dim, z_dim, dx=1, dy=1, dz=1):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.z_dim = z_dim
        
        self.open_nodes = []
        self.closed_nodes = []

    def dist(self,n1, n2):
        d = (((n1.loc.x-n2.loc.x)*self.dx)**2
             + ((n1.loc.y-n2.loc.y)*self.dy)**2
             + ((n1.loc.z-n2.loc.z)*self.dz)**2)**0.5

        return(d)

    def check_match(self, n1, n2):
        '''This function checks whether the coordinates of two given nodes
        match, and thereby whether one is a duplicate of the other.'''
        if (n1.loc.x == n2.loc.x
            and n1.loc.y == n2.loc.y
            and n1.loc.z == n2.loc.z):
            
            match = True
        else:
            match = False
        return(match)

    def check_existence(self, n):
        '''This function checks for the existence of a given node, n,
        in the open_nodes and closed_nodes lists.'''
        exists = False
        for elem in self.open_nodes:
            exists = self.check_match(elem, n)
            if exists:
                break
            else:
                pass
            for elem in self.closed_nodes:
                exists = self.check_match(elem, n)
                if exists:
                    break
                else:
                    pass
        return exists
    
    def close_node(self, n, end):
        # temporary variables for current node
        x = n.loc.x
        y = n.loc.y
        z = n.loc.z

        # Explore x dimension
        gcost = self.dx
        if x-1 >= 0:
            new = node(si.col_vec([x-1,y,z]))
            exists = self.check_existence(new)
            if exists == False:
                hcost = self.dist(new, end)
                new.open_node(gcost, hcost, n)
                self.open_nodes.append(new)
            else:
                pass
        if x+1 < self.x_dim:
            new = node(si.col_vec([x+1,y,z]))
            exists = self.check_existence(new)
            if exists == False:
                hcost = self.dist(new, end)
                new.open_node(gcost, hcost, n)
                self.open_nodes.append(new)
            else:
                pass

        # Explore y dimension
        gcost = self.dy
        if y-1 >= 0:
            new = node(si.col_vec([x,y-1,z]))
            exists = self.check_existence(new)
            if exists == False:
                hcost = self.dist(new, end)
                new.open_node(gcost, hcost, n)
                self.open_nodes.append(new)
            else:
                pass
        if y+1 < self.y_dim:
            new = node(si.col_vec([x,y+1,z]))
            exists = self.check_existence(new)
            if exists == False:
                hcost = self.dist(new, end)
                new.open_node(gcost, hcost, n)
                self.open_nodes.append(new)
            else:
                pass
                
        # Explore z dimension
        gcost = self.dz
        if z-1 >= 0:
            new = node(si.col_vec([x,y,z-1]))
            exists = self.check_existence(new)
            if exists == False:
                hcost = self.dist(new, end)
                new.open_node(gcost, hcost, n)
                self.open_nodes.append(new)
            else:
                pass
        if z+1 < self.z_dim:
            new = node(si.col_vec([x,y,z+1]))
            exists = self.check_existence(new)
            if exists == False:
                hcost = self.dist(new, end)
                new.open_node(gcost, hcost, n)
                self.open_nodes.append(new)
            else:
                pass
                
        self.closed_nodes.append(self.open_nodes.pop(0))
                
    def sort_nodes(self):
        self.open_nodes.sort(key=lambda x: x.fcost, reverse=False)
                
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
    w_env.open_nodes.append(start_node)

    try:
        while path_complete == False:
            w_env.sort_nodes()
            if w_env.check_match(w_env.open_nodes[0], goal_node):
                print("Found the end.")
                path = [w_env.open_nodes[0]]
                while (path[-1].parent != None):
                    path.append(path[-1].parent)
                    
                print("Finished the path")
                break
            
            w_env.close_node(w_env.open_nodes[0], goal_node)
            print("Open nodes: ", len(w_env.open_nodes))
            print("Closed nodes: ", len(w_env.closed_nodes))
            
    except IndexError:
        print("All nodes opened.")
    for elem in path:
                elem.print_node()
        
            
            
    


        
    
                
        
    
