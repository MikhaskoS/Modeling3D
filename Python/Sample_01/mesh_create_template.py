# низкоуровневое построение меша
import bpy
from bpy.types import Mesh, Object, Collection
from typing import Tuple, List


def mesh_new(name: str) -> Mesh:
    '''
    создаем mesh
    '''
    if name in bpy.data.meshes:
        mesh = bpy.data.meshes[name]
        mesh.clear_geometry()
    else:
        mesh = bpy.data.meshes.new(name)
    return mesh


def obj_new(mesh_name: str, mesh: Mesh) -> Object:
    '''
    создаем объект
    '''
    if mesh_name in bpy.data.objects:
        obj = bpy.data.objects[mesh_name]
        assert obj.type == 'MESH'
        obj.data = mesh
    else:
        obj = bpy.data.objects.new(mesh_name, mesh)

    return obj


def ob_to_col(obj: Object, col: Collection) -> None:
    '''
    отвязка от всех коллекций и от всех мастер коллекций
    привязка к нужной коллекции
    '''
    for c in bpy.data.collections:
        if obj.name in c.objects:
            col.objects.unlink(obj)

    for s in bpy.data.scenes:
        if obj.name in s.collection.objects:
            sc.collection.objects.unlink(obj)

    col.objects.link(obj)


def mesh_pydata() -> Tuple[List[Tuple]]:
    verts = [
        (-1.0, -1.0, -1.0),
        (-1.0,  1.0, -1.0),
        (1.0, 1.0, -1.0),
        (1.0, -1.0, -1.0),
        (-1.0, -1.0, 1.0),
        (-1.0,  1.0, 1.0),
        (1.0, 1.0, 1.0),
        (1.0, -1.0, 1.0)
    ]

    faces = [
        (0, 1, 2, 3),
        (7, 6, 5, 4),
        (4, 5, 1, 0),
        (7, 4, 0, 3),
        (6, 7, 3, 2),
        (5, 6, 2, 1)]

    edges = []

    # for i,f in enumerate(faces):
    #   faces[i] = tuple(reversed(f))

    return verts, faces, edges


def create_obj():
    mesh_name = "TEST"
    col_name = "Test Pydata"
    # assert col_name in bpy.data.collection
    col = bpy.data.collections[col_name]

    mesh = mesh_new(mesh_name)
    # assert type(mesh) == Mesh
    obj = obj_new(mesh_name, mesh)
    # assert type(obj) == Object
    ob_to_col(obj, col)

    pydata = mesh_pydata()
    mesh.from_pydata(vertices=pydata[0], faces=pydata[1], edges=pydata[2])


if __name__ == "__main__":
    create_obj()
