import bpy

# пример
# перемещение на субкадр 50.5 - если нужно что-то сделать
# до кадра 50
bpy.context.scene.frame_set(50, subframe = .5)

# обязательные аргументы для handler
def move_object_on_x(self, context):
    frame = bpy.context.scene.frame_current_final
    bpy.data.objects['Cube'].location[0] = frame
    
    #for ob in bpy.data.objects:
    #    if ob.name.startswith('Cube') and ob.type == 'MESH':
    #        ob.location[0] += frame
    
    #bpy.data.objects['Cube'].location[0] += frame

# очистка (нужно быть внимательным, чтобы не очистить,
# например, функции какого-нибудь аддона)
bpy.app.handlers.frame_change_pre.clear()

# добавление функции в обработчик событий (смена кадра)
bpy.app.handlers.frame_change_pre.append(move_object_on_x)