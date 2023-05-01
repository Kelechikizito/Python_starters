# A PROGRAM THAT DETERMINES THE ADMISSION PRICES OF ZOO GUESTS
a = []
b = []
price = 0

while True:
    age = input('Enter the age of each guest(Enter a blank line to cancel): ')
    b.append(age)
    if b[0] == '': break
    if age == '':
        c = sum(a)
        print('The admission cost of the group is ${:.2f}'.format(c))
        break
    elif int(age) <= 2:
        price = 0
        a.append(price)
    elif (int(age) >= 3) and (int(age) <= 12):
        price = 14
        a.append(price)
    elif (int(age) > 12) and (int(age) < 65):
        price = 23
        a.append(price)
    elif (int(age) >= 65):
        price = 18
        a.append(price)
    