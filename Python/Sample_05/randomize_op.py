'''
Для выбранного объекта случайным
образом изменить масштаб 
'''
import bpy
from random import randint
from typing import List
from bpy.types import Operator, Panel, PropertyGroup, Object
from bpy.utils import register_class, unregister_class
from bpy.props import (BoolProperty, IntProperty, FloatProperty,
                       StringProperty, PointerProperty)

class RandomProps(PropertyGroup):
    change_even : BoolProperty(
        name = 'Увеличить пипку', 
        default = True)
    minx : FloatProperty(
        name = 'Min X', 
        soft_min = 0,
        soft_max = 2,
        subtype = 'FACTOR',
        default = 0.2)
    maxx : FloatProperty(
        name = 'Max X',  
        soft_min = 0,
        soft_max = 2,
        subtype = 'FACTOR',
        default = 0.2)
    miny : FloatProperty(name = 'Min X', default = 0.2)
    maxy : FloatProperty(name = 'Max X', default = 0.2)
    minz : FloatProperty(name = 'Min Z', default = 0.2)
    maxz : FloatProperty(name = 'Max Z', default = 0.2)
    

class RandomScale(Operator):

    # обязательные параметры
    bl_idname = "myop.randscale" 
    bl_label = "Randomize Scale"
    change_even = None
    minx = None
    maxx = None
    miny = None
    maxy = None
    minz = None
    maxZ = None
    
    
    def structure(self, context):
        self.scene = context.scene
        #props = context.object.rand # привязываем свойства к панели
        props = context.scene.rand # привязываем свойства к панели
        self.change_even = props.change_even
        self.minx = props.minx
        self.maxx = props.maxx
        self.miny = props.miny
        self.maxy = props.maxy
        self.minz = props.minz
        self.maxz = props.maxz
        
    def get_random(self, min : float, max : float) -> float:
        return randint(int(min * 100), int(max * 100)) / 100
    
    def get_selected_objects(self) -> List[Object]:
        return [ob for ob in self.scene.objects if ob.select_get()]
    
    def randomize(self): 
        objects = self.get_selected_objects()
        for ob in objects:
            sc_x = self.get_random(self.minx, self.maxx)
            if self.change_even:
                ob.scale = (sc_x, sc_x, sc_x)
            else:
                sc_y = self.get_random(self.miny, self.maxy)
                sc_z = self.get_random(self.minz, self.maxz)
                ob.scale = (sc_x, sc_y, sc_z)
        
        
        # обязательный метод
    def execute(self, context):
        #raise NotImplementedError
        #--------------------
        print("EXECUTED!")
        self.structure(context)
        self.randomize()

        #--------------------
        return {'FINISHED'}
    
class OBJECT_PT_RandomizeScalePanel(Panel):
    bl_label = 'Randomize Scale'
    bl_space_type = 'VIEW_3D'   # где
    bl_region_type = 'UI'
    bl_category = 'Rand'        # отображаемое имя
    
    def draw(self, context):
        layout = self.layout
        #props = context.object.rand # привязываем свойства к панели
        props = context.scene.rand # привязываем свойства к панели
        col = layout.column()
        col.prop(props, 'change_even')
        
        col = layout.column()
        col.prop(props, 'minx')
        col.prop(props, 'maxx')
        
        col = layout.column()
        spl = col.split()
        spl.prop(props, 'miny')
        spl.prop(props, 'maxy')
    
        col = layout.column()
        box = col.box()
        spl = box.split(align = True)
        spl.enabled = not props.change_even
        spl.prop(props, 'minz')
        spl.prop(props, 'maxz')
        
        row = layout.row()
        row.operator('myop.randscale')
        
    

classes =[
    RandomProps,  # первый
    RandomScale,
    OBJECT_PT_RandomizeScalePanel
]

def register():
    for cl in classes:
        register_class(cl)
    # наше свойство (rand) для pby.types.Object
    # теперь в свойстве rand будут содержаться все свойства,
    # которые определены в RandomProps
    #bpy.types.Object.rand = PointerProperty(type = RandomProps)
    bpy.types.Scene.rand = PointerProperty(type = RandomProps)
        
def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
        

if __name__ == '__main__':
    register()
    #bpy.ops.myop.randscale()