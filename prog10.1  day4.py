#Quessing game from youtube

import random
import math

lower = int(input('Enter the lower limit: '))
upper = int(input('Enter the upper limit: '))

guess = int(input('Guess a number: '))

if guess < lower or guess > upper:
    print('Please enter your number between your range: ')
else:
    randomNumber = random.randint(lower, upper)
    chance = round(math.log(upper-lower+1, 2))

    while chance > 0:
        chance = chance - 1
        if guess > randomNumber: 
            print('Too high')
        elif guess < randomNumber: 
            print('Too low')
        else:
            print('you guessed it right, the number is,', randomNumber)
            break
        if chance != 0:
            print('you have only', chance, 'chances left')
            guess = int(input('Guess a number: '))
        else:
            print('you have exhausted all your chances')






