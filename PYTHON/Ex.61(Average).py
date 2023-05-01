# A PROGRAM THAT CALCULATES THE AVERAGE OF VALUES ENTERED BY THE USER
val = int(input('Enter 0 to indicate end of values\nEnter each number: '))
a = []  # MAKING A LIST OUT OF VAL COS INTEGER IS NOT AN ITERABLE
count = 1   # THIS INDICATES THE NUMBER OF VALUES AT THE STAGE
a.append(val)   #APPENDING INTEGER TO AN ITERABLE FOR THE AVERAGE CALCULTION
if val == 0:
    print('INVALID NUMBER TO BEGIN WITH\nEnter 0 to indicate end of values')
else:
    while val:
         val1 = int(input('Enter each number: '))
         a.append(val1)
         count += 1     # LOOP ADDS ONE AT EVERY LOOP(REPETITION)
         if val1 == 0:
             count -= 1     # 1 IS SUBTRACTED FROM TOTAL NO OF VALUES SINCE 0 WAS ENTERED
             avg = sum(a)/ count 
             print(avg, 'is the average of values entered')
             break
