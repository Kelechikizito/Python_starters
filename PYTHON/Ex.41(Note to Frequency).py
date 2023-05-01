# A PROGRAM THAT READS MUSICAL NOTES AND CONVERTS THEM TO FREQUENCY
read = input('What musical note are you playing?\nTry one of these:C4, D4, E4, F4, G4, A4, B4:  ')
if read == 'C4':
    print('261.63Hz is the frequency')
elif read == 'D4':
    print('293.66Hz is the frequency')
elif read == 'E4':
    print('329.63Hz is the frequency')
elif read == 'F4':
    print('349.23Hz is the frequency')
elif read == 'G4':
    print('392.00Hz is the frequency')
elif read == 'A4':
    print('440.00Hz is the frequency')
elif read == 'B4':
    print('493.88Hz is the frequency')
else:
    print('Not a musical note!')
if read == 'C4' or 'D4' or 'E4' or 'F4' or 'G4' or 'A4' or 'B4':
    octave = int(read[1])     # THIS EXPRESSION INDEXES THE READ THEN CHANGES IT TO INTEGER
else:
    print('ERROR! CROSSCHECK YOUR MUSICAL NOTE TO CONTINUE.')
if read == 'C4':
    freq = 261.63
elif read == 'D4':
    freq = 293.66
elif read == 'E4':
    freq = 329.63
elif read == 'F4':
    freq = 349.23
elif read == 'G4':
    freq = 329.00
elif read == 'A4':
    freq = 440.00
elif read == 'B4':
    freq = 493.88
else:
    print('Crosscheck your musical note')
freq_oct = freq / 2 ** (4 - octave)         # THIS BRINGS OUT THE FREQUENCY IN ITS CORRECT OCTAVE
print('The frequency of {} in its correct octave is {} Hz.'.format(read, freq_oct))


