import print_axes as pa
import sanitize_inputs as si

red = (1,0,0)
blue = (0,0,1)
green = (0,1,0)

csys_list = []

root_origin = si.col_vec([0,0,0])

root = pa.csys('Root', pa.auto_get_T(root_origin.vec,'x',0))
root.set_color(red)
csys_list.append(root)

A = pa.csys('A', pa.get_T(), root)
A.set_color(blue)
csys_list.append(A)

B = pa.csys('B', pa.get_DH_T(), A)
B.set_color(green)
csys_list.append(B)

pa.plot_csys(csys_list)
