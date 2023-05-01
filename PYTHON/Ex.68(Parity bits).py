# A PROGRAM THAT COMPUTES PARITY BITS

a = []


while True:
    line = input('Enter 8 bits(Enter blank to terminate): ')
    a.append(line)
    if a[0] == '':
        break
    elif line == '':
        break
    elif line.count('0') + line.count('1') != 8:
        print('This is not 8 bits\nTry again')
    elif line.count('0') + line.count('1') == 8:
        ones = line.count('1')
        if ones % 2 == 0:
            print('The parity bit should be 0')
        else:
            print('The parity bit should be 1')