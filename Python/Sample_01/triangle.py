import bpy
import math


radian_step = 0.1
current_radius = 0.1
number_triangles = 50

for i in range(1, number_triangles):
    # add triangle
    current_radius = current_radius + radian_step
    bpy.ops.mesh.primitive_circle_add(vertices = 3, radius = current_radius)

    # ссылка на активный объект
    triangle_mesh = bpy.context.active_object

    # поворот
    degrees = -90
    radians =  math.radians(-90)
    triangle_mesh.rotation_euler.x = radians

    # конвертируем
    bpy.ops.object.convert(target = 'CURVE')

    # скос
    triangle_mesh.data.bevel_depth = 0.05
    triangle_mesh.data.bevel_resolution = 16

    # сглаживание
    bpy.ops.object.shade_smooth()