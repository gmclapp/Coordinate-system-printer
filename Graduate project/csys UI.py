import print_axes as pa
import sanitize_inputs as si
import robotics

red = (1,0,0)
blue = (0,0,1)
green = (0,1,0)
some_other_color = (0.25,0.5,0.75)

color_list = []
for i in range(3):
    color_list.append((1-0.33*i, 0+0.33*i,0))
                      
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
# The following loop generates strings with which to name frames
for index, T in enumerate(T_list):
    if index > 0:
        parent = new_csys_list[index-1] # Sets frame parent
        new = pa.csys("T"+str(index), T, parent) # Name frame
    else:
        # sets the root as parent for the first frame
        new = pa.csys("T"+str(index), T, root) 

    new.set_color(color_list[index])
    new_csys_list.append(new)
    
csys_list += new_csys_list # Add new frames to the list to be printed
for T in csys_list:
    T.resolve()
    # This calculates the HT matrix with respect to the root. This is
    # required for printing.

pa.plot_csys(csys_list)
