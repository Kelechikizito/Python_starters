# A PROGRAM THAT NAMES A TRIANGLE
side1 = int(input('Enter the length of one side of the triangle: '))
side2 = int(input('Enter the length of the second side of the triangle: '))
side3 = int(input('Enter the length of the third side of the triangle: '))
if side1 == side2 == side3:
    print('This is an equilateral triangle')
elif (side1 == side2) or (side2 == side3) or (side3 == side1):
    print('This is an isoceles triangle')
else:
    print('This is a scalene triangle')