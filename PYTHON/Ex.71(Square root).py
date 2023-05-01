# A PROGRAM THAT COMPUTES AND DISPLAYS SQUARE ROOTS OF NUMBERS

x = int(input('Enter a number: '))
number = 1

while number * number != x:
    number += 1


guess = number

while True:
    guess = (guess + (x/guess))/2
    print(guess, 'is the square root')
    break