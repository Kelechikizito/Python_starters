#  A PROGRAM THAT COMPUTES ARITHMETRICAL OPERATIONS
from cmath import log10
from importlib import import_module


a = int(input('Type in your first integer: '))
b = int(input('Type in your second integer: '))
sum = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b
import math
log = math.log10(a)
exponential = a ** b
print('The sum is', sum)
print('The difference is', difference)
print('The product is', product)
print('The quotient is', quotient)
print('The remainder from division is', remainder)
print('The log is', log)
print('The exponential is', exponential)

