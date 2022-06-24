#Rock > scissors, Scissors > paper, Paper > Rock

import random

choices = ['rock', 'paper', 'scissors']

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper or scissors? ')

    if player == computer:
        print('Player: ', player)
        print('Computer: ', computer)
        print('its a tie!')

    elif player == 'rock':
        if computer == 'scissors':
            print('Player: ', player)
            print('Computer: ', computer)
            print('you win!')

        if computer == 'paper':
            print('Player: ', player)
            print('Computer: ', computer)
            print('you lose!')
            
    elif player == 'paper':
        if computer == 'rock':
            print('Player: ', player)
            print('Computer: ', computer)
            print('you win!')

        if computer == 'scissors':
            print('Player: ', player)
            print('Computer: ', computer)
            print('you lose!')

    elif player == 'scissors':
        if computer == 'paper':
            print('Player: ', player)
            print('Computer: ', computer)
            print('you win!')

        if computer == 'rock':
            print('Player: ', player)
            print('Computer: ', computer)
            print('you lose!')

    
        



   

