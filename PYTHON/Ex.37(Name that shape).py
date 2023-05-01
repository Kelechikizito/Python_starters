# A PROGRAM THAT NAMES A SHAPE
no_of_sides = int(input('Enter the number of sides of the shape(3 - 10): '))
if no_of_sides == 3:
    print('You have a triangle')
elif no_of_sides == 4:
    print('You have a quadilateral')
elif no_of_sides == 5:
    print('You have a pentagon')
elif no_of_sides == 6:
    print('You have a hexagon')
elif no_of_sides == 7:
    print('You have a heptagon')
elif no_of_sides == 8:
    print('You have an octagon')
elif no_of_sides == 9:
    print('You have a nonagon')
elif no_of_sides == 10:
    print('You have a decagon')
else:
    print('OUT OF RANGE!')