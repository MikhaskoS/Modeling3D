import math

print('----- Cl01 -------') 
class Cl_01(object): 
    x = 23 
    
print(Cl_01.x) 
#------------------------------------------
# дескрипторы
print('----- Cl02 -------') 
class Cl_02(object): 
    def __init__(self, value):
        self.value = value
    def __set__(self, *_):
        pass
    def __get__(self, *_):
        return self.value
    
    def hell(self):
        print ('Hello!')
    
class X(object):
    c = Cl_02(23)

x = X()
print(x.c)   #23
x.c = 42
print(x.c)   #23
#------------------------------------------
print('----- Cl03 -------') 
class Cl_03(object):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._area = None
        
    @property                                 # свойство
    def area(self):
        '''площадь прямоугольника'''
        self._area = self.width * self.height 
        return self._area
    
    @area.setter
    def area(self, value):
        print("setter of x called")
        scale = math.sqrt(value / self.area)
        self.width *= scale
        self.height *= scale
    
    @area.deleter
    def area(self):
        print("deleter of area called")
        del self._area

    
    def astatic(): print('a static method')  # статический метод
    astatic = staticmethod(astatic)
    
    @staticmethod
    def bstatic(): print('b static method')  # статический метод
    
    
    
obA = Cl_03(5, 6)
Cl_03.astatic()
Cl_03.bstatic()

print(obA.area)
obA.area = 3
print(obA.area)

del(obA.area)