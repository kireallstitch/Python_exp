# import random
#
#
# def flip():
#     return bool(random.randint(0, 1))
#
#
# def find_streak(count):
#     current_ht = flip()
#     current_streak = 1
#     for i in range(1, count - 1):
#         next_ht = flip()
#         if current_ht == next_ht:
#             current_streak += 1
#         else:
#             current_streak = 1
#             current_ht = next_ht
#         if current_streak == 6:
#             return 1
#     return 0
#
#
# numberOfStreaks = 0
# for experimentNumber in range(10000):
#     # Код, создающий список из 100 значений 'heads' или 'tails'
#     numberOfStreaks += find_streak(100)
#     # Код, который проверяет, есть ли полоса из 6 орлов или решек подряд.
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))
#
#

import random

#variable declaration

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    CoinFlip = [] #### (1) create a new, empty list for this list of 100
    for i in range(100):
        CoinFlip.append(random.randint(0,1))
    #does not matter if it is 0 or 1, H or T, peas or lentils. I am going to check if there is multiple 0 or 1 in a row

    #### # (6) example / test
    #### # if uncommented should be 100%
    #### CoinFlip = [ 'H', 'H', 'H', 'H', 'H', 'H', 'T', 'T', 'T', 'T', 'T', 'T' ]

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 1 #### (2, 4) any flip is a streak of (at least) 1; reset for next check
    for i in range(1, len(CoinFlip)): #### (3) start at the second flip, as we will look back 1
        if CoinFlip[i] == CoinFlip[i-1]:  #checks if current list item is the same as before
            streak += 1
        else:
            streak = 1 #### (2) any flip is a streak of (at least) 1

        if streak == 6:
            numberOfStreaks += 1
            break #### (5) we've found a streak in this CoinFlip list, skip to next experiment
                  #### if we don't, we get percentages above 100, e.g. the example / test above
                  #### this makes some sense, but is likely not what the book's author intends

print('Chance of streak: %s%%' % (numberOfStreaks / 100.0))