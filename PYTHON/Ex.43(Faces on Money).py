# A PROGRAM THAT READS DENOMINATION OF THE MONETRAY NOTES BRING THE EQUIVALENT FACES
gw = 1
tj = 2
al = 5
ah = 10
aj = 20
usg = 50
bf = 100
read = int(input('What is the denomination of your dollar banknote? '))
if read == gw:
    print('George Washington is on the 1 dollar')
elif read == tj:
    print('Thomas Jefferson is on the 2 dollar')
elif read == al:
    print('Abraham Lincoln is on the 5 dollar')
elif read == ah:
    print('Alexander Hamilton is on the 10 dollar')
elif read == aj:
    print('Andrew Jackson is on the 20 dollar')
elif read == usg:
    print('Ulysees S. Grant is on the 50 dollar')
elif read == bf:
    print('Benjamin Franklin is on the 100 dolar')
else:
    print("{} dollar doesn't exist".format(read))