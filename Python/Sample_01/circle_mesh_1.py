import bpy
import math
import pprint  # форматированное представление объектов

# initialize paramaters
vert_count = 32  # show with 16 and 64
angle_step = math.tau / vert_count
radius = 2

# create a list of vert coordinates
vert_coordinates = list()

# repeat code in a loop
for i in range(vert_count):

    # calculate current current_angle
    current_angle = angle_step * i

    # calculate coordinate
    x = radius * math.cos(current_angle)
    y = radius * math.sin(current_angle)

    # visualize what we are doing
    bpy.ops.mesh.primitive_ico_sphere_add(radius=0.05, location=(x, y, 0))

    # add current coordinate to list
    vert_coordinates.append((x, y, 0))

pprint.pprint(vert_coordinates)