# A PROGRAM THAT CONVERTS GRADE POINT TO A LETTER GRADE
aplus = 4.0
a = 4.0
aminus = 3.7
bplus = 3.3
b = 3.0
bminus = 2.7
cplus = 2.3
c = 2.0
cminus = 1.7
dplus = 1.3
d = 1.0
f = 0
point = float(input('Enter your Grade Point: '))
if (point >= aplus):
    print('You have an A+')
elif (point > aminus) and (point < a):
    print('You have an A')
elif (point >= 3.5) and (point <= aminus):
    print('You have an A-')
elif (point > b) and (point <= 3.4):
    print('You have a B+')
elif (point <= b) and (point > bminus):
    print('You have a B')
elif (point >= 2.5) and (point <= bminus):
    print('You have a B-')
elif (point > c) and (point <= 2.4):
    print('You have a C+')
elif (point <= c) and (point > cminus):
    print('You have a C')
elif (point >= 1.5) and (point <= 1.7):
    print('You have a C-')
elif (point > d) and (point <= 1.4):
    print('You have a D+')
elif (point <= d) and (point > 0.5):
    print('You have a D')
elif (point <= 0.4):
    print('You have an F')