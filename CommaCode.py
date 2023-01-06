spam = [
    'apples', 'bananas',
    'tofu', 'cats'
]


def spam_and():
    try:
        spam[-1] = 'and ' + spam[-1]
    except IndexError:
        print('empty list')


spam_and()
print(', '.join(spam))
