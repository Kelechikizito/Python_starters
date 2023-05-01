#  A PROGRAM THAT BRING THE POINT OF A GRADE
F = 0
D = 1.0
DPLUS = 1.3
CMINUS = 1.7
C = 2.0
CPLUS = 2.3
BMINUS = 2.7
B = 3.0
BPLUS = 3.3
AMINUS = 3.7
A = 4.0
APLUS = 4.0
point = (input('Enter your grade: '))
if point == 'F':
    print('You have 0 point')
elif point == 'D':
    print('You have 1.0 point')
elif point == 'D+':
    print('You have 1.3 points')
elif point == 'C-':
    print('You have 1.7 points')
elif point == 'C':
    print('You have 2.0 points')
elif point == 'C+':
    print('You have 2.3 points')
elif point == 'B-':
    print('You have 2.7 points')
elif point == 'B':
    print('You have 3.0 points')
elif point == 'B+':
    print('You have 3.3 points')
elif point == 'A-':
    print('You have 3.7 points')
elif point == 'A':
    print('You have 4.0 points')
elif point == 'A+':
    print('You have 4.0 points')
else:
    print('INVALID GRADE!')