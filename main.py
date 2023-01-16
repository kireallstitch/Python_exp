ran = int(input('Range? >'))
verif = ran / 2
array = [0]*ran
for i in range(ran):
    item = int(input("Data = >"))
    array[i] = item
if (isinstance(verif, float)):
    print(True)
    midpoint = int(verif + 1.5)
    median = array[(midpoint)]
print(median)