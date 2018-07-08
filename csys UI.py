import print_axes as pa
import sanitize_inputs as si
import database_functions as df
import robotics

red = (1,0,0)
blue = (0,0,1)
green = (0,1,0)
some_other_color = (0.25,0.5,0.75)

csys_list = []

root_origin = si.col_vec([0,0,0])

# root coordinate system
root = pa.csys('Root', pa.auto_get_T(root_origin.vec,'x',0))
root.set_color(red)
csys_list.append(root)
##
### homogeneous transform method
##A = pa.csys('A', pa.get_T(), root)
##A.set_color(blue)
##csys_list.append(A)
##
### Denavit-Hartenberg(DH) convention
##B = pa.csys('B', pa.get_DH_T(), A)
##B.set_color(green)
##csys_list.append(B)

# DH method from file
robot_file = open("robot_config.csv", mode='r')
alpha1 = float(df.vlookup(robot_file, 1, 0, 1))
print("Alpha1: ", alpha1)
robot_file.seek(0)
a1 = float(df.vlookup(robot_file, 1, 0, 2))
robot_file.seek(0)
theta1 = float(df.vlookup(robot_file, 1, 0, 3))
robot_file.seek(0)
d1 = float(df.vlookup(robot_file, 1, 0, 4))

C = pa.csys('C', robotics.DH(alpha1, a1, theta1, d1), root)
C.set_color(some_other_color)
csys_list.append(C)



pa.plot_csys(csys_list)
