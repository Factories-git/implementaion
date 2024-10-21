n, m = map(int, input().split())
r, c, dir = map(int, input().split())
room = []
time = 0
cleaner = [r, c]


def is_clean(r, c):
    if room[r + 1][c] == room[r - 1][c] == room[r][c + 1] == room[r][c - 1] == 2:
        return True
    if (room[r+1][c] == 1 and room[r - 1][c] == room[r][c + 1] == room[r][c - 1] == 2) or (room[r - 1][c] == 1 and room[r + 1][c] == room[r][c + 1] == room[r][c - 1] == 2)or (room[r][c+1] == 1 and room[r + 1][c] == room[r - 1][c] == room[r][c - 1] == 2) or (room[r-1][c] == 1 and room[r + 1][c] == room[r][c + 1] == room[r][c - 1] == 2):
        return True
    return False


def is_wall(r, c):
    if room[r + 1][c] == room[r - 1][c] == room[r][c + 1] == room[r][c - 1] == 1:
        return True
    return False


def change_dir():
    global dir
    if dir == 0:
        dir = 3
    elif dir == 3:
        dir = 2
    elif dir == 2:
        dir = 1
    else:
        dir = 0


for i in range(n):
    room.append(list(map(int, input().split())))

while True:
    if room[cleaner[0]][cleaner[1]] == 0:
        time += 1
        room[cleaner[0]][cleaner[1]] = 2
    if is_clean(cleaner[0], cleaner[1]) or is_wall(cleaner[0], cleaner[1]):
        if room[cleaner[0]+1][cleaner[1]] != 1:
            cleaner[0] += 1
        else:
            break
    else:
        change_dir()
        if dir == 0:
            if room[cleaner[0]+1][cleaner[1]] == 0:
                cleaner[0] += 1
        elif dir == 1:
            if room[cleaner[0]][cleaner[1]+1] == 0:
                cleaner[1] += 1

        elif dir == 2:
            if room[cleaner[0] - 1][cleaner[1]] == 0:
                cleaner[0] -= 1
        else:
            if room[cleaner[0]][cleaner[1] - 1] == 0:
                cleaner[1] -= 1
        print(time, cleaner , '\n', room[cleaner[0]-1], '\n', room[cleaner[0]], '\n', room[cleaner[0]+1])