#  A PROGRAM THAT COMPUTES THE AREA OF A TRIANGLE
print('''The are of a triangle can be computed using the following formulae,
where b is the length of the base of the triangle, and h is its height
\t\tarea=b*h/2''')
b = float(input('Enter the length of the base in metres: '))
h = float(input('Enter the height of the triangle in metres: '))
a = (b*h)/2
print('The area of the triangle is {0:.2f} m2, the base length is {1}m and the height is {2}m'.format(a,b,h))
