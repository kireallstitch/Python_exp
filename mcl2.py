import pyperclip
from prettytable import PrettyTable

TEXT = {'y': """Хорошо, принял!""",
        'n': """Извините, но не могу""",
        'b': """Извините, сейчас занят""",
        'm': """Пожалуйста отправьте запрос на почту site2@vashdom-kras.ru""",
        'j': """Женя, запусти пожалуйста обработку :)""",
        '1': """Благодарим за ваш отзыв! Ждём Вас снова за покупками :)""",
        '2': """Спасибо, что оценили! Приходите к нам ещё :)""",
        '3': """Спасибо за обратную связь! Обязательно примем Ваше замечание во внимание! :)""",
        'v': """find . -type f -name 'local_i*' -exec awk 'tolower($0)~/success/ { print FILENAME":1:"$0 } { nextfile }' {} + | sort #ПРОВЕРКА ВЫГРУЗКИ""",
        'w': """curl wttr.in #ПОГОДА В ТЕРМИНАЛЕ"""}  # Keyphrase

table = PrettyTable()
table.field_names = ["Keyphrase", "Phrase"]
for key, value in TEXT.items():
    table.add_row([key, value])

print(table)
