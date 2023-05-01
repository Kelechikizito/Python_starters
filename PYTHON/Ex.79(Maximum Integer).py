# A PROGRAM THAT EXAMINES THE MAXIMUM VALUE IN A COLLECTION

from random import randrange
max = 100
y = randrange(1,101)
print(y)
update = 0

for x in range(1,100):
    x = randrange(1,101)
    if x > y:
        y = x   # y SUPPLANTS x AND ACTS AS THE CACHED MEMORY OF THE PREVIOUS X
        update += 1
        print(x,' <==  Update')
    else:
        print(x) 

print('The maximum value was {}'.format(y))      
print('The maximum value was updated {} times'.format(update))

