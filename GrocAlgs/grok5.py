ar = [2, 3, 7, 8, 10]
newar = []

for i in range(len(ar)):
    col = []
    for j in range(len(ar)):
        col.append(ar[i] * ar[j])
    newar.append(col)


print(*newar, sep='\n')