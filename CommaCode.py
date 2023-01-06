spam = [
        'apples', 'bananas',
        'tofu', 'cats'
        ]


def spamF(spam):
    spam.insert(3, 'and')
    print(*spam, sep=', ')
spamF(spam)
