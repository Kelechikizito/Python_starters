# A PROGRAM THAT DIFFERENTIATES BETWEEN OLD AND NEW LICENSE PLATES
license = input('Enter the license plate: ')
if (len(license) == 6) and (((license[0] >='A' and license[0] <= 'Z')
    and (license[1] >= 'A' and license[1] <= 'Z') and (license[2] >= 'A' and license[2] <= 'Z'))
    and ((license[3] >= '0' and license[3] <= '9') 
    and (license[4] >= '0' and license[4] <= '9') and (license[5] >= '0' and license[5] <= '9'))):
    print('THIS IS AN OLD LICENSE PLATE')
elif (len(license) == 7) and (((license[0] >= '0' and license[0] <= '9') 
    and (license[1] >= '0' and license[1] <= '9') and (license[2] >= '0' and license[2] <= '9')
    and (license[3] >= '0' and license[3] <= '9')) and
    ((license[4] >= 'A' and license[4] <= 'Z') and (license[5] >= 'A' and license[5] <= 'Z')
    and (license[6] >= 'A' and license[6] <= 'Z'))):
    print('THIS IS A NEW LICENSE PLATE')
else:
    print('INVALID LICENSE PLATE')