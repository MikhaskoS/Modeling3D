import bpy
import math


bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object

start_frame = 1
end_frame = 150

cube.keyframe_insert("rotation_euler", frame = start_frame)

degrees = 360
radians = math.radians(degrees)
cube.rotation_euler.z = radians

cube.keyframe_insert("rotation_euler", frame = end_frame)