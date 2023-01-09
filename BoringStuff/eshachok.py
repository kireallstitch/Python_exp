# Знаменитая игра против ИИ!!!!
import random, sys
print('КАМЕНЬ! НОЖНИЦЫ! БУМАГА! ЕШАЧОК!')
# These variables keep track of the number of wins, losses, and ties.
win = 0
lose = 0
tire = 0
while True:  # The main game loop.
    print('%s Побед, %s Проебов, %s Вничью' % (win, lose, tire))
    while True:  # The player input loop.
        print('Enter your move: (к)амень (б)умага (н)ножницы or (в)ыйти')
        playerMove = input()
        if playerMove == 'в':
            sys.exit()  # Quit the program.
        if playerMove == 'к' or playerMove == 'б' or playerMove == 'н':
            break  # Break out of the player input loop.
        print('Type one of к, б, н, or в.')
    # Display what the player chose:
    if playerMove == 'к':
        print('КАМЕНЬ versus...')
    elif playerMove == 'б':
        print('БУМАГА versus...')
    elif playerMove == 'н':
        print('НОЖНИЦЫ versus...')
    # Display what the computer chose:
    randomNumber = computerMove = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'к'
        print('КАМЕНЬ')
    elif randomNumber == 2:
        computerMove = 'б'
        print('БУМАГА')
    elif randomNumber == 3:
        computerMove = 'н'
        print('НОЖНИЦЫ')
    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('Ничья!')
        tire = tire + 1
    elif playerMove == 'к' and computerMove == 'н':
        print('ЗаебОк!')
        win = win + 1
    elif playerMove == 'б' and computerMove == 'к':
        print('ЗаебОк!')
        win = win + 1
    elif playerMove == 'н' and computerMove == 'б':
        print('ЗаебОк!')
        win = win + 1
    elif playerMove == 'к' and computerMove == 'б':
        print('пизДА!')
        lose = lose + 1
    elif playerMove == 'б' and computerMove == 'н':
        print('пизДА!')
        lose = lose + 1
    elif playerMove == 'н' and computerMove == 'к':
        print('пизДА!')
        lose = lose + 1
