# A LOOP PROGRAM THAT CONVERTS DECIMAL TO BINARY

dec = int(input('Enter a decimal number(base 10): '))
result = ''


while dec != 0:
    r = dec % 2
    result += str(r)
    dec = dec // 2

print(result[-1::-1], 'is the equivalent binary number.')   # THE PURPOSE OF THE NEGATIVE DOUBLE SLICING IS TO READ THE STRING BACKWARDS