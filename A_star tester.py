import sanitize_inputs as si
import A_star

print("Enter the coordinates of the obstacle.")
o_pos = si.get_coords()
o_r = si.get_real_number("Enter the radius of the obstacle")
o_h = si.get_real_number("Enter the height of the obstacle")

print("Enter the starting position.")
start = si.get_coords()

print("Enter the payload position.")
end = si.get_coords()

obst = A_star.obstacle(o_pos, o_r, o_h)

path = A_star.generate_path(start, end, obst)
