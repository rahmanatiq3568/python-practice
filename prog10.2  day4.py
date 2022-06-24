#Quessing game
#This program - will ask for lower & upper limit, 
#if the number is above range it will show warning,
#by pressing '00', this game can be quit.

import random

print('To quit, press 00: ')
score = 0
lower = int(input('Enter the lower limit: '))
upper = int(input('Enter the upper limit: '))

while True:
    num = random.randint(lower,upper)
    guess = int(input('Guess a number: '))

    guess_num = guess
    if guess_num  is num:
        print('Congrats, you guessed it correctly.')
        score += 10
        print('your score is: ', score)
    elif guess == 00:
        print('Game over')
        break
    
    elif guess < lower or guess > upper:
        print('Please enter your number between your range! ')
    else:
        print('you lose')
        print('the number is: ', num)
        
        

        