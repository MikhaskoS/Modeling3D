import bpy
import math
import random


def create_mesh():
    bpy.ops.mesh.primitive_cube_add()

    obj = bpy.context.active_object

    obj.scale.x = obj.scale.x * 0.5
    obj.scale.y = obj.scale.y * 2
    obj.scale.z = obj.scale.z * 0.1

    random_rotation = random.uniform(0, 360)
    obj.rotation_euler.z = math.radians(random_rotation)

    bpy.ops.object.transform_apply()

    return obj


def update_obj_transform(obj, current_angle):

    obj.location.z += obj.dimensions.z                          # размер объекта
    obj.rotation_euler.z = math.radians(current_angle)


def animate_rotation(obj, current_frame, rotation_frame_count):
    obj.animation_data_clear()                                  #очистка анимации
    
    obj.keyframe_insert("rotation_euler", frame = current_frame)

    obj.rotation_euler.z += math.radians(360)
    frame = current_frame + rotation_frame_count

    obj.keyframe_insert("rotation_euler", frame=frame)


def create_next_layer(current_angle, current_frame, rotation_frame_count):
    # duplicate the mesh
    bpy.ops.object.duplicate(linked=True)

    # get a reference to the currently active object
    obj = bpy.context.active_object

    update_obj_transform(obj, current_angle)

    animate_rotation(obj, current_frame, rotation_frame_count)


def main():
    obj = create_mesh()

    angle_step = 3
    current_angle = angle_step

    current_frame = 1
    frame_step = 1
    rotation_frame_count = 90

    animate_rotation(obj, current_frame, rotation_frame_count)

    while current_angle <= 360:

        create_next_layer(current_angle, current_frame, rotation_frame_count)

        current_angle += angle_step

        current_frame += frame_step

    # конечный кадр
    bpy.context.scene.frame_end = current_frame + rotation_frame_count


main()