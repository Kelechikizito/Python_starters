# A PROGRAM THAT COMPUTES THE ROOTS OF A QUADRATIC FUNCTION
print('''A quadratic function has the form:
        f(x)=ax^2 + bx + c''')
a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))
from cmath import sqrt
import math
s = sqrt((b**2) - 4*(a * c))
root1 = (-b + s) / (2 * a) 
root2 = (-b - s) / (2 * a)
if (root1 == 0) and (root2 == 0):
    print('There are no real roots')
elif (root1 != 0) and (root2 != 0):
    print('There are two real roots and they are {} and {}'.format(root1, root2))
elif (root1 != 0) and (root2 == 0):
    print('There is just one real root and it is {}'.format(root1))
elif (root1 == 0) and (root2 != 0):
    print('There is just one real root and it is {}'.format(root2))