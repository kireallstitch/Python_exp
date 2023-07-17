import random
import sys
import time
import keyboard

print('Магический Шар приветствует тебя')
print('Нажмите на кнопку ПРОБЕЛ, что бы потрясти шар')
print('НАЖМИТЕ НА КНОПКУ ESC, ЧТО БЫ ВЫЙТИ')


def get_answer(answernumber):
    if answernumber == 1:
        return 'Это несомненно!'
    elif answernumber == 2:
        return 'Это однозначно так!'
    elif answernumber == 3:
        return 'Да!'
    elif answernumber == 4:
        return 'Ответ не ясен! Спроси ещё раз!'
    elif answernumber == 5:
        return 'Спроси попозже!'
    elif answernumber == 6:
        return 'Мой ответ нет!'
    elif answernumber == 7:
        return 'Сконцентрируйся! И спроси ещё!'
    elif answernumber == 8:
        return 'Прогноз не утешительный!'
    elif answernumber == 9:
        return 'Очень сомневаюсь!'


while True:

    if keyboard.is_pressed('esc'):
        sys.exit()
    elif keyboard.is_pressed(' '):

        print(f'{get_answer(random.randint(1, 9)):#^50}')
        time.sleep(0.5)
        print('Магический шар приветствует тебя')
        print('Нажмите на кнопку ПРОБЕЛ, что бы потрясти шар')
        print('Нажмите на кнопку esc, что бы выйти')
        continue
