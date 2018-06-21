import sanitize_inputs as si
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

Ptip0 = si.col_vec([10.45,7.227,0])
R0to3 = get_R('z', 119)

Pw2t = si.col_vec([3,0,0])

Pw2t0 = np.dot(R0to3,Pw2t.vec)
Pwrist = Ptip0.vec - Pw2t0

print(Pwrist)
