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
L2 = 15
w1z = 3
w2z = 4
theta1_list = [0,0,20]
theta2_list = [0,90,50]

omega1 = np.array([0,0,w1z])
omega2 = np.array([0,0,w2z])

pos1 = np.array([L1,0,0])
pos2 = np.array([L2,0,0])

vel1 = np.cross(omega1, pos1) # velocity of link1 tip in frame 1

for i in range(len(theta1_list)):
    R01 = get_R('z', theta1_list[i])
    R12 = get_R('z', theta2_list[i])
    R02 = np.dot(R01,R12)

    omega2in2 = omega2 + np.dot(R12, omega1)
    vel2 =np.dot(R12,np.cross(omega1, pos1)) + np.cross(omega2in2, pos2) # velocity of link 2 tip in frame 2
    
    v2in1 = vel1 + np.dot(R12, vel2)
    print(v2in1)
    
    

    

    
