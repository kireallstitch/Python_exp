spam = [
        'a', 'b',
        'x', 'y',
]


def comma_join(spam):
    if len(spam) == 0:
        return ''
    if len(spam) == 1:
        return str(spam[0])
    spam[-1] = 'and ' + spam[-1]
    return str(', '.join(spam))


print(comma_join(spam))
