import random,sys,time,keyboard

print('Магический шар приветсвует тебя')
print('Нажмите на кнопку ПРОБЕЛ, что бы потрясти шар')
print('Нажмите на кнопку esc, что бы выйти')


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Это несомненно!'
    elif answerNumber == 2:
        return 'Это однозначно так!'
    elif answerNumber == 3:
        return 'Да!'
    elif answerNumber == 4:
        return 'Ответ не ясен! Спроси ещё раз!'
    elif answerNumber == 5:
        return 'Спроси попозже!'
    elif answerNumber == 6:
        return 'Мой ответ нет!'
    elif answerNumber == 7:
        return 'Сконцентрируйся! И спроси ещё!'
    elif answerNumber == 8:
        return 'Прогноз не утешительный!'
    elif answerNumber == 9:
        return 'Очень сомневаюсь!'

while True:

    if keyboard.is_pressed('esc'):
        sys.exit()
    elif keyboard.is_pressed(' '):


        print('____________'+ getAnswer(random.randint(1, 9))+'_______________')
        time.sleep(0.4)
        print('Магический шар приветсвует тебя')
        print('Нажмите на кнопку ПРОБЕЛ, что бы потрясти шар')
        print('Нажмите на кнопку esc, что бы выйти')
        continue
