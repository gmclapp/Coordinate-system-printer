import print_axes as pa
import sanitize_inputs as si
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
T_list=pa.DH_from_file(robot_file)
robot_file.close()

new_csys_list=[]
for index, T in enumerate(T_list):
    try:
##        new_csys_list.append(pa.csys("T"+str(index), T, new_csys_list[index-1]))
        new_csys_list.append(pa.csys("T"+str(index), T, root))
        new_csys_list[-1].set_color(some_other_color)
    except IndexError:
        new_csys_list.append(pa.csys("T"+str(index), T, root))


csys_list += new_csys_list

pa.plot_csys(csys_list)
