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

    return(obst, start, end, n)

def auto_entry():
    o_pos = si.col_vec([2,2,0])
    o_r = 1.1
##    o_h = float('Inf')
    o_h = 50

    obst = A_star.obstacle(o_pos, o_r, o_h)

    start = A_star.node(si.col_vec([0,5,0]))

    end = A_star.node(si.col_vec([5,1,0]))

    n = 25

    return(obst, start, end, n)

obst, start, end, n = auto_entry()
##obst, start, end, n = manual_entry()

t0 = time.time()

error_flag = False

print("Checking path ends")    
temp1 = obst.collision_detect(start)
temp2 = obst.collision_detect(end)
error_flag = temp1 or temp2
print("Done checking.")

if not error_flag:
    path = A_star.generate_path(start, end, n, obst)
    t1 = time.time()
    print("Time: ",t1-t0)
    print("Path:", path)
else:
    print("path end point unreachable.")
