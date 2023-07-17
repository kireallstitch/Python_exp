#! python3
# mclip.py - A multi-clipboard program.
TEXT = {'agree': """Хорошо, принял!""",
        'busy': """Извините, сейчас занят""",
        'mail': """Не могли бы вы отправить запрос на почту site2@vashdom-kras.ru"""}


import pyperclip
print('Input keyphrase'.center(40 + 40, '*'))


def printKeyphrase(TEXT):
    print('KEY PHRASES'.center(40 + 40, '-'))
    for k, v in TEXT.items():
        print(k.ljust(10, '=') + str(v).rjust(70, '='))

while True:
    keyphrase = input(str())  # first command line arg is the keyphrase
    if keyphrase in TEXT:
        pyperclip.copy(TEXT[keyphrase])
        print('Text for ' + keyphrase + ' copied to clipboard.')
    else:
        print(('There is no text for '+ keyphrase).center(40 + 40, '!'))
        printKeyphrase(TEXT)
