import random
answer = random.randint(1, 100)
 
while True:
    first_step = int(input('make a guess from one to hundred: '))

    if first_step == answer:
        print(f'that is the correct answer \n The answer is  {first_step}')
        break

    elif first_step < answer:
        print(f'the number you chos is too low')

        
    elif first_step > answer:
            print(f'the number you chose is too high') 
