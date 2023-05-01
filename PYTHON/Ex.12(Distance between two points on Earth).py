# PROGRAM THAT CALCUATES THE DISTANCE BETWEEN TWO POINTS ON EARTH
earth_radius = 6371.01
from cmath import acos, cos, sin
import math
t1 = math.degrees(int(input('ENTER THE LATITUDE OF POINT 1: ')))
t2 =  math.degrees(int(input('ENTER THE LATITUDE OF POINT 2: ')))
g1 =  math.degrees(int(input('ENTER THE LONGITUDE OF POINT 1: ')))
g2 =  math.degrees(int(input('ENTER THE LONGITUDE OF POINT 2: ')))
distance = ( earth_radius * acos(sin(t1)* sin(t2) + cos(t1) * cos(t2) * cos(g1-g2)))
print('The distance between the two points is' ,distance, 'km')
print('''FOR VERIFICATION PURPOSES THIS IS THE FORMULAE BELOW 
earth_radius * arcos(sin(t1)* sin(t2) + cos(t1) * cos(t2) * cos(g1-g2)''')