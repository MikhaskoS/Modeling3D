import bpy
from bpy.types import Operator, Object
from bpy.utils import register_class, unregister_class
from bpy.props import (IntProperty, FloatProperty,
                       StringProperty, PointerProperty)


class MyOperator(Operator):
    # обязательные параметры
    bl_idname = "myop.exe"
    bl_label = "MyOperator"

    a: IntProperty()
    f: FloatProperty()
    t: StringProperty(default="Hello, Blender")
    # obj : PointerProperty(type = Object)

    # обязательный метод
    def execute(self, context):
        # --------------------
        print("EXECUTED!")
        if (self.text):
            print(self.t)

        # --------------------
        return {'FINISHED'}


classes = [
    MyOperator
]


def register():
    for cl in classes:
        register_class(cl)


def unregister():
    for cl in reversed(classes):
        unregister_class(cl)


if __name__ == '__main__':
    register()
    bpy.ops.myop.exe()
