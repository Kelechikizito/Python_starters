# A PROGRAM THAT IMPLEMENTS MULTIPLE WORD PALINDROMES

import string

while True:
    word = input('Enter a word: ')
    space = word.replace(' ', '')
    case = space.lower()
    mark = case.translate(str.maketrans('', '', string.punctuation))
    if word[:] == word[-1::-1]:
        print('You entered a palindrome')
        break
    elif space[:] == space[-1::-1]:
        print('You entered a palindrome')
        break
    elif case[:] == case[-1::-1]:
        print('You entered a palindrome')
        break
    elif mark[:] == mark[-1::-1]:
        print('You entered a palindrome')
        break
    else:
        print("\nYou didn't enter a palindrome, try again.\n")