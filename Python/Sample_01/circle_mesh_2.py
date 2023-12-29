import bpy
import math
import pprint


def get_circle_vert_coordinates(vert_count, radius):

    angle_step = math.tau / vert_count

    # create a list of vert coordinates
    vert_coordinates = list()

    # repeat code in a loop
    for i in range(vert_count):

        current_angle = angle_step * i

        x = radius * math.cos(current_angle)
        y = radius * math.sin(current_angle)

        vert_coordinates.append((x, y, 0))

    pprint.pprint(vert_coordinates)
    
    return vert_coordinates
    
    
def create_circle_mesh(vert_coordinates, vert_count):
    
    verts = vert_coordinates
    edges = []
    for i in range(vert_count):
        current_vert_index = i
        next_vert_index = (i + 1) % vert_count   # красивый обход цикла
        edges.append((current_vert_index, next_vert_index))
        print(f"{current_vert_index}<->{next_vert_index}")
    
    faces = []

    mesh_data = bpy.data.meshes.new("circle_data")
    mesh_data.from_pydata(verts, edges, faces)

    mesh_obj = bpy.data.objects.new("circle_obj", mesh_data)
    return mesh_obj

    
vert_count = 32 
radius = 2
vert_coordinates = get_circle_vert_coordinates(vert_count, radius)
mesh_obj = create_circle_mesh(vert_coordinates, vert_count)

bpy.context.collection.objects.link(mesh_obj)