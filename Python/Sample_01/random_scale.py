import bpy, random, time

def random_scale():
    t1 = time.perf_counter()
    
    #for object in bpy.data.objects:
    #    scale = random.randint(5, 100)/100
    #    object.scale = (scale, scale, scale)
    
    # если в проекте создана коллекция Cubes и нас 
    # интересуют только объекты внутри нее
    for object in bpy.data.collections['Cubes'].objects:
        scale = random.randint(5, 100)/100
        object.scale = (scale, scale, scale)    
    
    t2 = time.perf_counter()
    print(t2 - t1)
    
random_scale()