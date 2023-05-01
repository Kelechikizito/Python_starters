#  A PROGRAM THAT COMPUTES THE BODY MASS INDEX OF AN INDIVIDUAL
print(' A PROGRAM THAT COMPUTES THE BODY MASS INDEX OF AN INDIVIDUAL')
height = float(input('Enter your height in metres: '))
weight = float(input('Enter your weight in kilograms: '))
BMI = weight / (height * height)
print('Your Body Mass Index(BMI) is {}'.format(BMI))