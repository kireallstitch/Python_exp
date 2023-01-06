spam = [
        'apples', 'bananas',
        'tofu', 'cats'
        ]


def spamF(spam):
    spam.insert(-1, 'and')
    print(*spam, sep=', ')
spamF(spam)
