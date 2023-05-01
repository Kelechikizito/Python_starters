# A PROGRAM THAT PERFORMS A COIN FLIP SIMULATION

import random

coin = 'TH'
result = ''
y = 0
avg = []

while y < 10:
    flip = random.choice(coin)
    result += flip
    if (len(result) >= 3) and (result[-1] == result[-2]) and (result[-2] == result[-3]):
        length = len(result)
        avg.append(length)
        space = result.replace('', ' ')
        print('{} ({} flips)'.format(space, length))
        result = ''
        y += 1

average = sum(avg)/10
print(' On average, {} flips were needed.'.format(average))