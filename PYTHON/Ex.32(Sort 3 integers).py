# A PROGRAM THAT SORTS THREE INTEGERS
# from math import sort


int1 = int(input('Enter the first integer: '))
int2 = int(input('Enter the second integer: '))
int3 = int(input('Enter the third integer: '))
int = []
int.append(int1)
int.append(int2)
int.append(int3)

# int = [int1, int2, int3]
sorted = sorted(int)
print(sorted,'is the ascending order.')