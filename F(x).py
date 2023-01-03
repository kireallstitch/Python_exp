+def F(x):
    return x ** 2
for x in range(-10, 10):
    print('Для F('+str(x) + ') = '+str(F(x)))
i = -3
while i < 3:
    print('Для F(' + str(i) + ') = ' + str(F(i)))
    i = i + 0.1