# A PROGRAM THAT DISPLAYS 15 APPROXIMATIONS OF PI


pi = 0

for term in range(15):

    if term == 0:
        pi += 3
        print(pi)
    else:
        sign = (-1) ** (term + 1)
        d = 2*term
        den = (d) * (d + 1) * (d + 2)
        pi += (sign) * (4/den)
        print(pi)
    
    



