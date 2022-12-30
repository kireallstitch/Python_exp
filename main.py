print('enter number')
number = int(input())

def collatz(number):
    if number % 2 == 0:
        number = int(number // 2)

    elif number % 2 == 1:
        number = int(3 * number + 1)
    return number
while number != 1:
    print(number)
    number = collatz(number)
    if number == 1:
        print(number)
        break
