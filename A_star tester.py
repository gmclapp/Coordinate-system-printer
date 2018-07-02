import sanitize_inputs as si
import A_star
import time

def manual_entry():
    print("Enter the coordinates of the obstacle.")
    o_pos = si.get_coords()
    o_r = si.get_real_number("Enter the radius of the obstacle >>> ", lower = 0)
    o_h = si.get_real_number("Enter the height of the obstacle. (leave blank for infinite height). >>> ", lower = 0)

    obst = A_star.obstacle(o_pos, o_r, o_h)

    print("Enter the starting position. >>> ")
    start = A_star.node(si.get_coords())

    print("Enter the payload position. >>> ")
    end = A_star.node(si.get_coords())

    n = si.get_integer("Enter the approximate number of nodes along the path. >>> ", lower = 0)
    
def auto_entry():
    o_pos = si.col_vec([2,2,0])
    o_r = 1.1
##    o_h = float('Inf')
    o_h = 50

    obst = A_star.obstacle(o_pos, o_r, o_h)

    start = A_star.node(si.col_vec([0,0,0]))

    end = A_star.node(si.col_vec([5,5,5]))

    n = 25

    return(obst, start, end, n)

t0 = time.time()

obst, start, end, n = auto_entry()

##print("Cool obstacle!\nIt is located at:\nX: ",
##      obst.loc.x,"\n",
##      "Y: ", obst.loc.y,"\n",
##      "Z: ", obst.loc.z,"\n",
##      "It has a radius:\nR: ", obst.r,"\n",
##      "It has a height:\nh: ", obst.h,"\n", sep='')

##print("Thanks, the robot gripper will start at:\nX: ",
##      start.loc.x,"\n",
##      "Y: ", start.loc.y,"\n",
##      "Z: ", start.loc.z,"\n",sep='')
##
##print("Ok, the payload will be retreived from:\nX: ",
##      end.loc.x,"\n",
##      "Y: ", end.loc.y,"\n",
##      "Z: ", end.loc.z,"\n",sep='')

print("Checking start node")    
obst.collision_detect(start)
print("Done checking.")

path = A_star.generate_path(start, end, obst)
t1 = time.time()
print("Time: ",t1-t0)
