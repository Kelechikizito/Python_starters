# A PROGRAM THAT HAS A RITCHER SCALE
magnitude = float(input('Enter the magnitude of the earthquake: '))
if magnitude < 2.0:
    print('This is a micro earthquake')
elif (magnitude == 2.0) or (magnitude < 3.0):
    print('This is a very minor earthquake')
elif (magnitude == 3.0) or (magnitude < 4.0):
    print('This is a minor earthquake')
elif (magnitude == 4.0) or (magnitude < 5.0):
    print('This is a light earthquake')
elif (magnitude == 5.0) or (magnitude < 6.0):
    print('This is a moderate earthquake')
elif (magnitude == 6.0) or (magnitude < 7.0):
    print('This is a strong earthquake')
elif (magnitude == 7.0) or (magnitude < 8.0):
    print('This is a major earthquake')
elif (magnitude == 8.0) or (magnitude < 10.0):
    print('This is a great earthquake')
else:
    print('This is a meteoric earthquake')