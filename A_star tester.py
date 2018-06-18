import sanitize_inputs as si
import A_star

print("Enter the coordinates of the obstacle.")
o_pos = si.get_coords()
o_r = si.get_real_number("Enter the radius of the obstacle >>> ")
o_h = si.get_real_number("Enter the height of the obstacle >>> ")

obst = A_star.obstacle(o_pos, o_r, o_h)
print("Cool obstacle!\nIt is located at:\nX: ",
      obst.loc.x,"\n",
      "Y: ", obst.loc.y,"\n",
      "Z: ", obst.loc.z,"\n",
      "It has a radius:\nR: ", obst.r,"\n",
      "It has a height:\nh: ", obst.h,"\n", sep='')

print("Enter the starting position. >>> ")
start = si.get_coords()

print("Enter the payload position. >>> ")
end = si.get_coords()

path = A_star.generate_path(start, end, obst)