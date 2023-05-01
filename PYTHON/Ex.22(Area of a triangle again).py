#  AREA OF A TRIANGLE WITH THREE SIDES
from cmath import sqrt
import math
s1 = int(input('Enter the length of the first side of the triangle in metres: '))
s2 = int(input('Enter the length of the second side in metres: '))
s3 = int(input('Enter the length of the third side in metres: '))
s = (s1 + s2 + s3)/2
area = sqrt(s*(s-s1) * (s-s2) * (s-s3))
print("The triangle's area is {:.2f} m2".format(area))