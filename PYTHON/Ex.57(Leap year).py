# A PROGRAM THAT DETERMINES IF A YEAR IS A LEAP YEAR
year = int(input('Enter a year: '))
f = year % 400
if (f == 0):
    print('This is a leap year')
elif (f % 100 == 0):
    print('This is not a leap year')
elif (f % 4 == 0):
    print('This is a leap year')
else:
    print('This is not a leap year')