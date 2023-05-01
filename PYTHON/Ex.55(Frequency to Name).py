# A PROGRAM THAT PUTS OUT THE NAME OF AN ELECTROMAGNETIC FREQUENCY RANGE
rw = 3 * 10**9
mw = 3 * 10**12
il = 4.3 * 10**14
vl = 7.5 * 10**14
uvl = 3 * 10**17
xr = 3 * 10**19
freq = int(input('Enter a frequency: '))
if freq < rw:
    print('This is a radio wave')
elif (freq >= rw) and (freq < mw):
    print('This is a microwave')
elif (freq >= mw) and (freq < il):
    print('This is an infrared light')
elif (freq >= il) and (freq < vl):
    print('This is a visible light')
elif (freq >= vl) and (freq < uvl):
    print('This is an ultraviolet light')
elif (freq >= uvl) and (freq < xr):
    print('This is an x-ray')
elif freq > xr:
    print('This is a gamma ray')