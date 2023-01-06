spam = [
        'q', 'w', 'e', 'r',
        't', 'y', 'u', 'i',
        'o', 'p', 'a', 's',
]


def spam_and():
    try:
        spam[-1] = 'and ' + spam[-1]
    except IndexError:
        print('empty list')


spam_and()
print(', '.join(spam))
