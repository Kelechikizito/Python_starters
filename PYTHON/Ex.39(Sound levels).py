# A PROGRAM THAT STATES VARIOUS SOUND LEVELS
jk = 130
glm = 106
ac = 70
qr = 40
decibel = int(input('Enter the sound level in decibels: '))
if decibel == jk:
    print('That is the noise level of a jackhammer')
elif decibel == glm:
    print('That is the noise level of a grass lawnmower')
elif decibel == ac:
    print('That is noise level of an alarm clock')
elif decibel == qr:
    print('That is the noise level of a quiet room')
elif decibel > jk:
    print('Your value is out of range(40-130)')
elif decibel > glm < jk:
    print('The noise level is between a jackhammer and a grass lawnmower')
elif decibel > ac < glm:
    print('The noise level is between a grass lawnmower and an alarm clock')
elif decibel > qr < ac:
    print('The noise level is between an alarm clock and a quiet room')
else:
    print('Your value is out of range(40 - 130)')