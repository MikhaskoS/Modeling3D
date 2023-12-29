import bpy
from bpy.types import Object, Collection

# Сотрим, какие объектв в сцене и распределяем их по созданным коллекциям

col_name_parent = "Test Collection"
col_name_monkey = "monkeys"
col_name_cube = "cubes"
col_name_ico = "icospheres"


def create_collection(col_name : str, parent_name = ''):
    '''
    Создание новой коллекции
    ''' 
    if(parent_name != ''):
        if parent_name not in bpy.data.collections:
            collection = bpy.data.collections.new(parent_name)
            scene_collection = bpy.context.scene.collection
            scene_collection.children.link(collection)
        else: pass   
        parent = bpy.data.collections[parent_name]

        if col_name not in parent.children:
            collection = bpy.data.collections.new(col_name)
            parent.children.link(collection)
    else: 
        if col_name not in bpy.data.collections:
            collection = bpy.data.collections.new(col_name)
            scene_collection = bpy.context.scene.collection
            scene_collection.children.link(collection)
            
def ob_to_col(obj : Object, col : Collection) -> None:
    '''
    отвязка от всех коллекций и от всех мастер коллекций
    привязка к нужной коллекции
    '''
    for c in bpy.data.collections:   # все коллекции, включая вложенные
        if obj.name in c.objects:
            c.objects.unlink(obj)
    
    for s in bpy.data.scenes:
        if obj.name in s.collection.objects:
            s.collection.objects.unlink(obj)
            
    col.objects.link(obj)

print('----')
create_collection(col_name_monkey, col_name_parent)
create_collection(col_name_cube, col_name_parent)
create_collection(col_name_ico, col_name_parent)

for obj in bpy.data.objects:
    if "Suz" in obj.name:
        destination_collection = bpy.data.collections[col_name_monkey]
        ob_to_col(obj, destination_collection)
    if "Cube" in obj.name:
        destination_collection = bpy.data.collections[col_name_cube]
        ob_to_col(obj, destination_collection)
    if "Icos" in obj.name:
        destination_collection = bpy.data.collections[col_name_ico]
        ob_to_col(obj, destination_collection)
