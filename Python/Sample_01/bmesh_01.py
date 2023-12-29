import bpy
import bmesh     # инструменты для работы с mesh

obj=bpy.context.object


print('-----------------------')
# координаты выбранных вершин
# их можно выбрать кодом v.select = True
if obj.mode == 'EDIT':
    bm = bmesh.from_edit_mesh(obj.data)
    for v in bm.verts:
        if v.select:
            print(v.co)      #  bm.verts[0].co = (2,2,2) - изм. коорд.
else:
    print("Object is not in edit mode.")