# A PROGRAM THAT IMPLEMENTS THE CEASER CIPHER

word = input('Enter a message(letters only): ')

for ch in word:
    if (ch == 'x'):
        ch = ord('a')
    elif (ch == 'X'):
        ch = ord('A')
    elif (ch == 'y'):
        ch = ord('b')
    elif (ch == 'Y'):
        ch = ord('B')
    elif (ch == 'z'):
        ch = ord('c')
    elif (ch == 'Z'):
        ch = ord('C')
    else:
        ch = ord(ch) + 3
    che = chr(ch)
    che = che.replace('#', ' ')
    print(che, end='')