"""
Creating a phyllotaxis pattern based on formula 4.1 from
http://algorithmicbotany.org/papers/abop/abop-ch4.pdf

Ф = n * 137.5     в градусах
r = c * sqrt(n)
"""
import bpy
import random
import math

ico_sphere_radius = 0.5
scale_fac = 1.0
angle = math.radians(random.uniform(137.0, 138.0))

# set angle to the Fibonacci angle 137.5 to get the sunflower pattern
# angle = math.radians(137.5)

count = 400

for n in range(count):
    # calculate "φ" in formula (4.1) http://algorithmicbotany.org/papers/abop/abop-ch4.pdf
    current_angle = n * angle

    # calculate "r" in formula (4.1) http://algorithmicbotany.org/papers/abop/abop-ch4.pdf
    current_radius = scale_fac * math.sqrt(n)

    # convert from Polar Coordinates (r,φ) to Cartesian Coordinates (x,y)
    x = current_radius * math.cos(current_angle)
    y = current_radius * math.sin(current_angle)

    # place ico sphere
    bpy.ops.mesh.primitive_ico_sphere_add(radius=ico_sphere_radius, location=(x, y, 0))