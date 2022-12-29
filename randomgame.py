# This is a guess the number game.
import random
secretNumber = random.randint(1, 100)
print('Я загадал число от 1 до 100.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('назови число.')
    guess = int(input())
    if guess < secretNumber:
        print('Твоё число маленькое.')
    elif guess > secretNumber:
        print('Твоё число большое.')
    else:
        break # This condition is the correct guess!
if guess == secretNumber:
    print('Супер! ты угадал ' + str(guessesTaken) + 'число!')
else:
    print('Нет! я загадал число ' + str(secretNumber))