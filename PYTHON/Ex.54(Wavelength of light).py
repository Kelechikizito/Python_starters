# A PROGRAM THAT READS THE WAVELENGTH OF VISIBLE LIGHT AND BRINGS OUT ITS RESPECTIVE COLOUR
wavelength = int(input('Enter the wavelength: '))
if (wavelength >= 380) and (wavelength < 450):
    print('The wavelength belongs to the Violet spectrum')
elif (wavelength >= 450) and (wavelength < 495):
    print('The wavelength belongs to the Blue spectrum')
elif (wavelength >= 495) and (wavelength < 570):
    print('The wavelength belongs to the Green spectrum')
elif (wavelength >= 570) and (wavelength < 590):
    print('The wavelength belongs to the Yellow spectrum')
elif (wavelength >= 590) and (wavelength < 620):
    print('The wavelength belongs to the Orange spectrum')
elif (wavelength >= 620) and (wavelength <= 750):
    print('The wavelength belongs to the Red spectrum')
else:
    print('INVALID WAVELENGTH.\nWavelength ranges from 380 to 750 nanometres.')