def shifting(c, k):
    global gears
    if c == 1:
        temp = gears[k][len(gears[k]) - 1]
        for i in range(len(gears[k]) - 1, 0, -1):
            gears[k][i] = gears[k][i - 1]

        gears[k][0] = temp
    else:
        temp = gears[k][0]
        for i in range(len(gears[k]) - 1):
            gears[k][i] = gears[k][i + 1]

        gears[k][len(gears[k]) - 1] = temp
    print(gears, k,c)
    if k != 3:
        if gears[k][2] != gears[k + 1][-3]:
            shifting(c * -1, k + 1)
        else:
            return
    else:
        return
    if k != 0:
        if gears[k][-2] != gears[k-1][2]:
            shifting(c * -1, k - 1)
        else:
            return
    else:
        return
    if gears[k][-2] == gears[k-1][2] and gears[k+1][-2] == gears[k][2]:
        return


gears = []
for i in range(4):
    gears.append(list(map(str, input())))
dir_change = []
for i in range(int(input())):
    dir_change.append(list(map(int, input().split())))
print(gears)
for n,d in dir_change:
    shifting(d,int(n)-1)

score = 0
if gears[0][0] == '1':
    score += 1
if gears[1][0] == '1':
    score += 2
if gears[2][0] == '1':
    score += 4
if gears[3][0] == '1':
    score += 8
print(gears)
print(score)