# A PROGRAM THAT DETERMINES A PALINDROME

while True:
    word = input('Enter a word: ')
    if word[:] == word[-1::-1]:
        print('You entered a palindrome')
        break
    else:
        print("You didn't enter a palindrome, try again.")