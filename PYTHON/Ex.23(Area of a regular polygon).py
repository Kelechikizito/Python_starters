#  A PROGRAM THAT COMPUTES THE AREA OFA REGULAR POLYGON
from cmath import pi, tan
import math


n = int(input('Enter the number of sides of the polygon: '))
s = float(input('Enter the length of a side of the polygon: '))
area = (n * s**2)/4 * tan(pi/n)
print('The area is {:.2f} m2.'.format(area))