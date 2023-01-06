spam = [
        'apples', 'bananas',
        'tofu', 'cats'
        ]


def spamand(spam):
    spam.insert(-1, 'and')
    print(*spam, sep=', ')
spamand(spam)
