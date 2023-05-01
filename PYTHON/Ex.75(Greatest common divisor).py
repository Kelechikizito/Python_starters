# A PROGRAM THAT DETERMINES THE GREATEST COMMON DIVISOR OF TWO COMMON INTEGERS

int1 = int(input('Enter a positive integer: '))
int2 = int(input('Enter a positive integer: '))
d = min(int1, int2)

while True:
    if ((int1 % d == 0) and (int2 % d == 0)):
        print(d, 'is the greatest common divisor')
        break
    else:
        d -= 1
        
