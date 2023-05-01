#  A FUNCTION THAT CALCULATES THE HYPOTENUSE OF A TRIANGLE

import math

def f(x, y):
    return math.sqrt((x**2) + (y**2))

x = float(input('Enter length of one of the short sides: '))
y = float(input('Enter length of the other short side: '))


print('The hypotenuse of the triangle is {:.2f}'.format(f(x, y)))
