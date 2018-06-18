import sanitize_inputs as si
import A_star

print("Enter the coordinates of the obstacle.")
o_pos = si.get_coords()
o_r = si.get_real_number("Enter the radius of the obstacle >>> ", lower = 0)
o_h = si.get_real_number("Enter the height of the obstacle >>> ", lower = 0)

obst = A_star.obstacle(o_pos, o_r, o_h)
print("Cool obstacle!\nIt is located at:\nX: ",
      obst.loc.x,"\n",
      "Y: ", obst.loc.y,"\n",
      "Z: ", obst.loc.z,"\n",
      "It has a radius:\nR: ", obst.r,"\n",
      "It has a height:\nh: ", obst.h,"\n", sep='')

print("Enter the starting position. >>> ")
start = A_star.node(si.get_coords())

print("Thanks, the robot gripper will start at:\nX: ",
      start.loc.x,"\n",
      "Y: ", start.loc.y,"\n",
      "Z: ", start.loc.z,"\n",sep='')

print("Enter the payload position. >>> ")
end = A_star.node(si.get_coords())

print("Ok, the payload will be retreived from:\nX: ",
      end.loc.x,"\n",
      "Y: ", end.loc.y,"\n",
      "Z: ", end.loc.z,"\n",sep='')

n = si.get_integer("Enter the approximate number of nodes along the path. >>> ", lower = 0)

obst.collision_detect(start)
move_length = A_star.dist(start, end)
dr = move_length/n

print("That move is",move_length,"long.\n The mesh resolution is",dr)

# path = A_star.generate_path(start, end, obst)
