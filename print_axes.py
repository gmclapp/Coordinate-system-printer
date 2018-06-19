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

class csys():
    def __init__(self, name, T, parent=None):
        ''' This function accepts a 4x4 homogeneous transform matrix and the
        name of a parent matrix. The tranformation will be applied to the parent
        and the origin and orientation of the new matrix will be supplied with
        respect to the inertial reference frame for the purpose of printing.'''
        
        # [from:to,from:to] slice includes from but not to
        # [rows,columns]
        self.name = name
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

    def find_limits(self):
        '''This function finds the extremes of the csys for the purpose of
        sizing the plot.'''

        # ux, uy, & uz are all unit vectors, so padding the origin by 2 is
        # garaunteed to show them.
        
        self.x_min = self.origin[0,0] - 2.0
        self.y_min = self.origin[0,1] - 2.0
        self.z_min = self.origin[0,2] - 2.0

        self.x_max = self.origin[0,0] + 2.0
        self.y_max = self.origin[0,1] + 2.0
        self.z_max = self.origin[0,2] + 2.0
    
    def get_plot_data(self):
        '''This function takes the unit vectors of the csys, and the location
        of the csys's origin and returns a 6 element row vector for printing.'''
        
        self.rx = np.column_stack([self.origin, self.ux])
        self.ry = np.column_stack([self.origin, self.uy])
        self.rz = np.column_stack([self.origin, self.uz])
        self.plot_data = np.row_stack([self.rx, self.ry, self.rz])
        return(self.plot_data)
        
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
    P_B_origin = si.get_coords()
    axis = si.get_letter("X, Y, or Z axis?",['x','X','y','Y','z','Z'])
    theta = si.get_real_number("Enter the angle of rotation in degrees. >>> ")
    R = get_R(axis, theta)
    T = robotics.HT_from_R_and_Porg(R, P_B_origin.vec)

    return(T)

def get_DH_T():
    alpha = si.get_real_number("Enter link twist (alpha) in degrees. >>> ")
    a = si.get_real_number("Enter link length (a). >>> ")
    theta = si.get_real_number("Enter link rotation (theta) in degrees. >>> ")
    d = si.get_real_number("Enter link offset (d). >>> ")

    T = robotics.DH(alpha, a, theta, d)

    return(T)

def auto_get_T(origin, axis, theta):
    '''This function generates a homogeneous transform matrix from a column
    vector for an origin, a string describing an axis of rotation, and
    an angle of rotation in degrees.'''
    R = get_R(axis, theta)
    print(R)
    T = robotics.HT_from_R_and_Porg(R, origin)
                               
    return(T)

red = (1,0,0)
blue = (0,0,1)
green = (0,1,0)

root_color = red
transformed_color = blue
second_tranform_color = green

root_origin = si.col_vec([0,0,0])

print(root_origin.vec)

root = csys('Root', auto_get_T(root_origin.vec,'x',0))
root.resolve()
root.get_plot_data()

A = csys('A', get_T())

A.resolve()
A.get_plot_data()
print(A.plot_data)

root.find_limits()
A.find_limits()

p_xmin = min(root.x_min, A.x_min)
p_xmax = max(root.x_max, A.x_max)
p_ymin = min(root.y_min, A.y_min)
p_ymax = max(root.y_max, A.y_max)
p_zmin = min(root.z_min, A.z_min)
p_zmax = max(root.z_max, A.z_max)

X, Y, Z, U, V, W = zip(*root.plot_data)
X1, Y1, Z1, U1, V1, W1 = zip(*A.plot_data)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(X, Y, Z, U, V, W, color=root_color)
ax.quiver(X1, Y1, Z1, U1, V1, W1, color=transformed_color)
ax.set_xlim([p_xmin, p_xmax])
ax.set_ylim([p_ymin, p_ymax])
ax.set_zlim([p_zmin, p_zmax])
plt.show()
