import bpy
from random import randint
from mathutils import Vector as Location # import и псевдоним
from mathutils import Vector as Rotation
from mathutils import Vector as Scale
from bpy.types import Object

class CustomObject():
    
    def __init__(self, ob : Object) -> None:
        self.ob = ob
        self.name = ob.name
        self.data = ob.data
        self.rotation = ob.rotation_euler
        self.scale = ob.scale 
    
    # аналог статического метода - можно вызывать
    # не создавая объект класса (можно переопределить 
    # при наследовании)
    @classmethodт
    def add(cls, a : int, b : int) -> int:
        return a + b
    
    # геттер
    @property
    def location(self) -> Location:
        return self.ob.location
    
    # сеттер
    @location.setter
    def location(self, loc : location) -> None:
        self.ob.location = loc
        
    # геттер
    @property
    def scale(self) -> Scale:
        return self.ob.scale
    
    # сеттер
    @location.setter
    def scale(self, sc : scale) -> None:
        self.ob.scale = sc
        
print(CustomObject.add(10, 20))
   
# выделенный объект в сцене     
objA = CustomObject(ob = bpy.context.object)

print(objA.location)
objA.location = Location((1, 5, 1))

# для всех объектов в сцене
def test1():
    for object in bpy.context.scene.objects:
        if not object.type == 'MESH':
            continue
        obj = CustomObject(object)
        locx = randint(-10, 10)
        locy = randint(-10, 10)
        locz = randint(-10, 10)
        obj.location = Location((locx, locy, locz))
        obj.scale = Scale(
            (randint(20, 200)/100, 
             randint(20, 200)/100, 
             randint(20, 200)/100))