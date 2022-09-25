from random import randint
def computer_choice():
    a = randint(1, 3)
    if a == 1:
        computer_move = 'r'
        print('Rock')
    elif a == 2:
        computer_move = 'p'
        print('Paper')
    elif a == 3:
        computer_move = 's'
        print('Scissors')
    return computer_move
def winner_decider(playermove, computer_move):
    if playermove == computer_move:
        print('It is a tie!')
        final = 't'
    elif playermove == 'r' and computer_move == 'p':
        print('You lose!')
        final = 'l'
    elif playermove == 'r' and computer_move == 's':
        print("You won!")
        final = 'w'
    elif playermove == 'p' and computer_move == 'r':
        print("You won!")
        final = 'w'
    elif playermove == 'p' and computer_move == 's':
        print('You lose!')
        final = 'l'
    elif playermove == 's' and computer_move == 'r':
        print("You lose!")
        final = 'l'
    elif playermove == 's' and computer_move == 'p':
        print("You won!")
        final = 'w'
    return final


win = 0
lose = 0
tie = 0

while True:
    playermove = ''
    # user choice:
    while playermove != 'r' and playermove != 'p' and playermove != 's' and playermove != 'q':
        print('Wins({}) Loses({}) Ties({})'.format(win,lose, tie))
        print('Enter your move: rock(r), paper(p), scissors(s), or quit(q)')
        playermove = input()
        if playermove != "r" and playermove != 'p' and playermove != 's':
            print('Type any one of the following: r for rock, s for scissor, p for paper and q for quitting the game.')

    if playermove == 'q':
        break



    if playermove == 'r':
        print('Rock versus ....')
    elif playermove == 'p':
        print('Paper versus ....')
    elif playermove == 's':
        print('Scissors versus ...')

    # computer choice
    computer_move = computer_choice()

    #Display win or lose or tie

    final = winner_decider(playermove,computer_move)
    if final == 'w':
        win += 1
    elif final == 'l':
        lose += 1
    else:
        tie += 1
print('the total number of wins are {}, loses are {}, and ties are {}.'.format(win, lose,tie))