#  !!!проблема!!!
#  ['prop'] - свойство объекта (Cuctom Properties), которое меняется
#  каждый кадр. Почему оно не работает как драйвер?

import bpy

# обязательные аргументы для handler
def move_object_on_x(self, context):
    frame = bpy.context.scene.frame_current_final
    bpy.data.objects['Cube']['prop'] = frame


# очистка (нужно быть внимательным, чтобы не очистить,
# например, функции какого-нибудь аддона)
#bpy.app.handlers.frame_change_pre.clear()

# добавление функции в обработчик событий (смена кадра)
if move_object_on_x not in bpy.app.handlers.frame_change_pre:
    bpy.app.handlers.frame_change_pre.append(move_object_on_x)