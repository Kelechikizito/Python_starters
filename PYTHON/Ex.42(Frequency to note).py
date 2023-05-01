# A PROGRAM THAT CONVERTS FREQUENCIES TO NOTESN
c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88
freq = float(input('What frequency are you playing? '))
if freq == c4:
    print('C4 is the equivalent musical note.')
elif freq == d4:
    print('D4 is the equivalent musical note.')
elif freq == e4:
    print('E4 is the equivalent musical note.')
elif freq == f4:
    print('F4 is the equivalent musical note.')
elif freq == g4:
    print('G4 is the equivalent musical note.')
elif freq == a4:
    print('A4 is the equivalent musical note.')
elif freq == b4:
    print('B4 is the equivalent musical note.')
else:
    print('Frequency does not correspond to a note.')