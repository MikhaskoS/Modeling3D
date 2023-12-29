import bpy
from bpy.types import Operator  
from bpy.utils import register_class, unregister_class

# построение собственного оератора
# наследуем от класса Operator
class ObjectScaleDouble(Operator):
    # обязательные параметры
    bl_idname = "my.double_scale"         # заглавные буквы недопустимы
    bl_label = "Object Scale Doule"
    
    # обязательный метод (только 2 аргумента)
    def execute(self, context):
        #--------------------
        print("Hello World")
        # применяется к выделенному объекту
        scale = context.object.scale
        scale *=2 
        #--------------------
        return {'FINISHED'}
        
    # спец. метод для проверки объекта на None
    # чтобы не появлялась ошибка, если объект не выбран
    @classmethod  #
    def poll(self, context):
        return context.object is not None
    

classes =[
    ObjectScaleDouble
]

def register():
    for cl in classes:
        register_class(cl)
        
def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
        
if __name__ == '__main__':
    register()
    # запускаем наш класс
    bpy.ops.my.double_scale()
