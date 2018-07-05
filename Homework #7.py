import robotics
import numpy as np
import sympy
##import robotics_sympy as rs
##
##th1, d, th3 = sympy.symbols(['theta1','d','theta3'])
##
##T01 = rs.DH(0, 0, th1, 5)
##T12 = rs.DH(-90, 0, 0, d)
##T23 = rs.DH(-90, 0, th3, 0)

sol1_T01 = robotics.prettymat(robotics.DH(0, 0, 64.1, 5))
sol1_T12 = robotics.prettymat(robotics.DH(-90, 0, -90, 3.7))
sol1_T23 = robotics.prettymat(robotics.DH(-90, 0, 17.91, 0))

sol2_T01 = robotics.prettymat(robotics.DH(0, 0, 64.1, 5))
sol2_T12 = robotics.prettymat(robotics.DH(-90, 0, -90, 7.506))
sol2_T23 = robotics.prettymat(robotics.DH(-90, 0, 162.091, 0))

sol1_T = sol1_T01*sol1_T12*sol1_T23

sol2_T = sol2_T01*sol2_T12*sol2_T23

P3tip = np.array([[0],[-2],[0],[1]])

#P_A = robotics.dot_list([T_AB, T_BC, T_CD, P_D])

P0sol1 = robotics.prettymat(robotics.dot_list([sol1_T01,
                                              sol1_T12,
                                              sol1_T23,
                                              P3tip]))

P0sol2 = robotics.prettymat(robotics.dot_list([sol2_T01,
                                              sol2_T12,
                                              sol2_T23,
                                              P3tip]))

##robotics.print_mat(sol1_T01)
##robotics.print_mat(sol1_T12)
##robotics.print_mat(sol1_T23)
##
##robotics.print_mat(sol2_T01)
##robotics.print_mat(sol2_T12)
##robotics.print_mat(sol2_T23)

