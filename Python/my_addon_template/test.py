import bpy
from mathutils import *
import bmesh

def IsSamePoint(v31, v32, limitDistance):
    if (v31 - v32).magnitude < limitDistance: return True

    return False


class Plane:
    @staticmethod
    def XY():
        p1 = Vector((0, 0, 0))
        p2 = Vector((1, 0, 0))
        p3 = Vector((0, 1, 0))

        return Plane(p1, p2, p3)


    # plane equation: (p - position).dot(normal) = 0
    def __init__(self, P1, P2, P3):
        self.normal = (P2 - P1).cross(P3 - P1)
        self.normal.normalize()

        self.position = P1

#--------------------------------------------
#--------------------------------------------
#--------------------------------------------
#print('hello')

#p1 = Vector((0, 0, 0))
#p2 = Vector((1, 0, 0))
#p3 = Vector((0, 1, 0))
#        
#plane = Plane(p1, p2, p3)

#print(plane.normal)

#-------------------------------
## Get the active mesh
#me = bpy.context.object.data


## Get a BMesh representation
#bm = bmesh.new()   # create an empty BMesh
#bm.from_mesh(me)   # fill it in from a Mesh


## Modify the BMesh, can do anything here...
#for v in bm.verts:
#    v.co.x += 1.0


## Finish up, write the bmesh back to the mesh
#bm.to_mesh(me)
#bm.free()  # free and prevent further access


#-------------------------------
print("----------")
obj = bpy.context.edit_object
me = obj.data

# Get a BMesh representation
bm = bmesh.from_edit_mesh(me)

bm.faces.active = None

# выбранные вершины
vert_list = [v for v in bm.verts if v.select]
        

# Modify the BMesh
x = True
y = False
z = True

x_median = 0
y_median = 0
z_median = 0

for i in range(0, len(vert_list)):
    x_median += vert_list[i].co.x
    y_median += vert_list[i].co.y
    z_median += vert_list[i].co.z

x_median /= len(vert_list)
y_median /= len(vert_list)
z_median /= len(vert_list)
   
for i in range(0, len(vert_list)):
    if x:
        vert_list[i].co.x = x_median
    if y:
        vert_list[i].co.y = y_median
    if z:
        vert_list[i].co.z = z_median


# Show the updates in the viewport
# and recalculate n-gon tessellation.
bmesh.update_edit_mesh(me, loop_triangles=True)