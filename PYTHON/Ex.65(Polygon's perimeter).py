# A PROGRAM THAT CALCULATES THE PERIMETER OF A POLYGON FROM COORDINATES ENTERED BY THE USER
x1 = int(input('Enter the x coordinate: '))
y1 = int(input('Enter the y cordinate: '))

from math import sqrt


while True:
    x2 = input('Enter the x coordinate: ')
    xint = int(x2)
    xdif = xint - x1
    y2 = input('Enter the y cordinate: ')
    yint = int(y2)
    ydif = yint - y1
    per = sqrt((xdif)**2 + (ydif)**2 )
    break

while True:
    x3 = input('Enter the x coordinate(blank to quit): ')
    xl = [] ; xl.append(x3)
    if xl[0] == '':
        print(per, 'is your perimeter')
        break
    if x3 == '':
        print(per2, 'is your perimeter')
        break
    xint1 = int(x3)
    xint1 -= int(x3)
    

    y3 = input('Enter the y coordinate: ')
    yint1 = int(y3)
    yint1 -= int(y3)
    per2 = sqrt((xint1 - xdif)**2 + (yint1 - ydif)**2 )
    

    

    
    
   
    
    

    