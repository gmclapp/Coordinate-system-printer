import robotics
import numpy as np

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

L1 = 20
w1z = 3
theta_list = [0,45,60,90]

omega1 = np.array([0,0,w1z])
pos1 = np.array([L1,0,0])

vel1 = np.cross(omega1, L1)

for th in theta_list:
    R = get_R('z',th)
    vel0 = np.dot(R, vel1)
    print(vel0)
    
