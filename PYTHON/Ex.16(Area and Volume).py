#   A PROGRAM THAT COMPUTES AREA AND VOLUME
from cmath import pi
import math
r = int(input('Enter your desired radius: '))
area_of_a_circle = pi * r**2
from fractions import Fraction
volume_of_a_sphere = Fraction(4, 3) * pi * r ** 3
print('{:.2f}'.format(area_of_a_circle),'m2 is the area of the circle')
print('{:.2f}'.format(volume_of_a_sphere),'m3 is the volume of the sphere')