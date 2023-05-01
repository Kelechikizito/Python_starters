# A PROGRAM THAT COMPUTES GPA
gp = 0
gpa = []

while True:
    grade  = (input('Enter a grade(press enter to quit): ')).upper()
    if grade == '': 
        cgpa = sum(gpa)/len(gpa)
        if cgpa > 3.0:
            print(cgpa,'is your CGPA, well done')
        if cgpa < 3.0:
            print(cgpa, 'is your CGPA work harder')
        break
    elif grade == 'F':
        gp = 0
        gpa.append(gp)
    elif grade == 'D':
        gp = 1.0
        gpa.append(gp)
    elif grade == 'D+':
        gp = 1.3
        gpa.append(gp)
    elif grade == 'C-':
        gp = 1.7
        gpa.append(gp)
    elif grade == 'C':
        gp = 2.0
        gpa.append(gp)
    elif grade == 'C+':
        gp = 2.3
        gpa.append(gp)
    elif grade == 'B-':
        gp = 2.7
        gpa.append(gp)
    elif grade == 'B':
        gp = 3.0
        gpa.append(gp)
    elif grade == 'B+':
        gp = 3.3
        gpa.append(gp)
    elif grade == 'A-':
        gp = 3.7
        gpa.append(gp)
    elif grade == 'A':
        gp = 4.0
        gpa.append(gp)
    elif grade == 'A+':
        gp = 4.0
        gpa.append(gp)
    else:
        print('')
        break
    
    
    




