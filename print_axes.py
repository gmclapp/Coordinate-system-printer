import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sanitize_inputs as si
import robotics

class row_vec():
    '''Retrieves a list of real number for x, y, and z from the user,
    and constructs a numpy row vector.'''
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self.vec = np.array([[self.x,self.y,self.z]])

class col_vec():
    '''Retrieves a list of real number for x, y, and z from the user,
    and constructs a numpy column vector.'''
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self.vec = np.array([[self.x],[self.y],[self.z]])

class csys():
    def __init__(self, origin, ux, uy, uz, parent = None, color = (1,0,0)):
        '''This function takes an origin point, and three unit vectors which
            define a coordinate system and calculates three rays for plotting
            using matplotlib.'''
        
        self.rx = np.column_stack([origin.vec, ux.vec])
        self.ry = np.column_stack([origin.vec, uy.vec])
        self.rz = np.column_stack([origin.vec, uz.vec])
        self.plot_data = np.row_stack([self.rx, self.ry, self.rz])

class csys2():
    def __init__(self, T, parent=None):
        # [from:to,from:to] slice includes from but not to
        # [rows,columns]
        self.T = T
        self.parent = parent
        self.origin = np.transpose(self.T[:-1,3:])

    def resolve(self):
        ''' This function will find the H.T. matrix relating self to the
        inertial csys through a string of parent csys as applicable for
        the purpose of printing'''
        
        if self.parent == None:
            print("No parent matrix specified.")
            self.ux = np.transpose(self.T[:-1,0:1])
            self.uy = np.transpose(self.T[:-1,1:2])
            self.uz = np.transpose(self.T[:-1,2:3])
        else:
            pass

    def get_plot_data(self):
        '''This function takes the unit vectors of the csys, and the location
        of the csys's origin and returns a 6 element row vector for printing.'''
        
        self.rx = np.column_stack([self.origin, self.ux])
        self.ry = np.column_stack([self.origin, self.uy])
        self.rz = np.column_stack([self.origin, self.uz])
        self.plot_data = np.row_stack([self.rx, self.ry, self.rz])
        return(self.plot_data)
        
def get_coords(rows=3):
    '''This function gets the coordinates for a point in 3D space from the user.
    It includes the error checking logic required to ensure the point's
    useability in subsequent functions.'''

    P_x = si.get_real_number("X >>>")
    P_y = si.get_real_number("Y >>>")
    P_z = si.get_real_number("Z >>>")

    point = col_vec([P_x,P_y,P_z])

    if rows == 3:
        return(point)
    elif rows == 4:
        point.vec = np.row_stack([point.vec,[1]])
        return(point)
    else:
        print("Invalid argument.")
        return(None)

def get_R(axis, angle):
    '''This function generates a 3x3 rotation matrix given an angle specified
    in degrees and an axis about which to rotate specified by a string 'x',
    'y', or 'z'.'''
    if axis.lower() == 'x':
        R = robotics.Rx(angle)
    elif axis.lower() == 'y':
        R = robotics.Ry(angle)
    elif axis.lower() == 'z':
        R = robotics.Rz(angle)

    return(robotics.prettymat(R))
        


def get_T():
    '''This function generates a homogeneous transform matrix given a position
    vector and a rotation describing the location of frame B with respect to
    frame A.'''
    
    print("Enter the position of frame B with respect to frame A.")
    P_B_origin = get_coords()
    axis = si.get_letter("X, Y, or Z axis?",['x','X','y','Y','z','Z'])
    theta = si.get_real_number("Enter the angle of rotation in degrees.")
    R = get_R(axis, theta)
    T = robotics.HT_from_R_and_Porg(R, P_B_origin.vec)

    return(T)

def get_DH_T():
    alpha = si.get_real_number("Enter link twist (alpha) in degrees.")
    a = si.get_real_number("Enter link length (a).")
    theta = si.get_real_number("Enter link rotation (theta) in degrees.")
    d = si.get_real_number("Enter link offset (d).")

    T = robotics.DH(alpha, a, theta, d)

    return(T)

def auto_get_T(origin, axis, theta):
    '''This function generates a homogeneous transform matrix from a column
    vector for an origin, a string describing an axis of rotation, and
    an angle of rotation in degrees.'''
    R = get_R(axis, theta)
    T = robotics.HT_from_R_and_Porg(R, origin)
                               
    return(T)

red = (1,0,0)
blue = (0,0,1)
green = (0,1,0)

root_color = red
transformed_color = blue

root_origin = row_vec([0,0,0])
root_ux = row_vec([1,0,0])
root_uy = row_vec([0,1,0])
root_uz = row_vec([0,0,1])

root = csys(root_origin, root_ux, root_uy, root_uz, color=red)
A = csys2(get_T())
A.resolve()
A.get_plot_data()
print(A.plot_data)

X, Y, Z, U, V, W = zip(*root.plot_data)
X1, Y1, Z1, U1, V1, W1 = zip(*A.plot_data)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(X, Y, Z, U, V, W, color=root_color)
ax.quiver(X1, Y1, Z1, U1, V1, W1, color=transformed_color)
ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
ax.set_zlim([0, 3])
plt.show()
