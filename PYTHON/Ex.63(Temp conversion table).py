# A PROGRAM THAT DISPLAYS A TEMPERATURE CONVERSION TABLE
fah = [32, 50, 68, 86, 104, 122, 140, 158, 176, 194]
cel = list(range(0, 100, 10))
print('Celsius\t\t\tFahrenheit')
for x,y in zip(cel, fah):
    print('{}\t\t\t{}.0'.format(x, y))