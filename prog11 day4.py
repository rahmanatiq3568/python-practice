#Rock, Paper, Scissors
#Rock > scissors, Scissors > paper, Paper > Rock
def rps_game (p1,p2):
    if p1 == p2:
        print("It's a tie")
    elif p1 == 'rock':
        if p2 == 'scissors':
            print('First player wins!')
        else:
            print('Second player wins!')
    elif p1 == 'scissors':
        if p2 == 'paper':
            print('First player wins!')
        else:
            print('Second player wins!') 
    elif p1 == 'paper':
        if p2 == 'rock':
            print('First player wins!')
        else:
            print('Second player wins!')
    else:
        print('invalid input!')
player1 = input('First player: rock, paper or scissors: ')
player2 = input('First player: rock, paper or scissors: ')


print(rps_game(player1, player2))