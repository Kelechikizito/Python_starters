# A PROGRAM THAT COMPUTES THE VOLUME OF A CYLINDER
from cmath import pi
import math
r = float(input('What is the radius of the circular base? '))
h = float(input('What is the height of the cylinder? '))
volume = (pi * r**2) * h
print('{0:.1f},{1}'.format(volume,'m3'),'is the volume of the cylinder')