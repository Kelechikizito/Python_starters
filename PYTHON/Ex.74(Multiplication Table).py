# A PROGRAM THAT DISPLAYS MULTIPLICATION TABLE

ze = 1; one = 1; two = 2; thr = 3; four = 4; five = 5
six = 6; sev= 7; ei = 8; nine = 9; ten = 10
print('\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(one, two, thr, four, five, six, sev, ei, nine, ten))
for x in range(10):
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(ze, one, two, thr, four, five, six, sev, ei, nine, ten))
    ze += 1
    one += 1
    two += 2
    thr += 3
    four += 4
    five += 5
    six += 6
    sev += 7
    ei += 8
    nine += 9
    ten += 10
