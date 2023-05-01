# A PROGRAM THAT DETERMINES THE PRIME FACTORS OF AN INTEGER

int = int(input('Enter an integer(2 or greater): '))
factor = 2

while factor <= int:
    if int % factor == 0:
        print(factor)
        int /= factor
    else:
        factor += 1
