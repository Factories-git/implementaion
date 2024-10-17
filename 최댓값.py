n_l = []
for i in range(9):
    n_l.append(list(map(int, input().split())))

max_ = 0
row = 0
idx = 0
for y in range(9):
    for x in range(9):
        if n_l[y][x] > max_:
            max_ = n_l[y][x]
            row = y
            idx = x
print(max_)
print(row+1, idx+1)
