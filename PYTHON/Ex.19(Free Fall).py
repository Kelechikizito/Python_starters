# A PROGRAM THAT CALCULATES THE FREE FALL OF AN OBJECT
from cmath import sqrt
print('acceleration = 9.8m/s2')
a = 9.8
u = 0
d = float(input('Enter the distance(in metres) at which the object travels: '))
import math
v = sqrt(u**2 + 2*a*d)
print('The final speed is {:.2f} m/s'.format(v))

