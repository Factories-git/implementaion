n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = []
time = 0
cleaner = [r, c]


def is_clean(r, c):
    # if room[r + 1][c] == room[r - 1][c] == room[r][c + 1] == room[r][c - 1] == 2:
    #     return True
    # if (room[r+1][c] == 1 and room[r - 1][c] == room[r][c + 1] == room[r][c - 1] == 2) or (room[r - 1][c] == 1 and room[r + 1][c] == room[r][c + 1] == room[r][c - 1] == 2)or (room[r][c+1] == 1 and room[r + 1][c] == room[r - 1][c] == room[r][c - 1] == 2) or (room[r-1][c] == 1 and room[r + 1][c] == room[r][c + 1] == room[r][c - 1] == 2):
    #     return True
    if any((room[r+1][c] == 0, room[r-1][c] == 0, room[r][c+1] == 0 , room[r][c-1] == 0)):
        return True
    return False


def is_wall(r, c):
    if room[r + 1][c] == 1 or room[r - 1][c] == 1 or room[r][c + 1] == 1 or room[r][c - 1] == 1:
        return True
    return False


def change_dir():
    global d
    if d == 0:
        d = 3
    elif d == 3:
        d = 2
    elif d == 2:
        d = 1
    else:
        d = 0


for i in range(n):
    room.append(list(map(int, input().split())))

while True:
    if room[cleaner[0]][cleaner[1]] == 0:
        time += 1
        room[cleaner[0]][cleaner[1]] = 2
    if is_clean(cleaner[0], cleaner[1]):
        change_dir()
        if d == 0:
            if room[cleaner[0]+1][cleaner[1]] == 0:
                cleaner[0] += 1
        elif d == 1:
            if room[cleaner[0]][cleaner[1]+1] == 0:
                cleaner[1] += 1

        elif d == 2:
            if room[cleaner[0] - 1][cleaner[1]] == 0:
                cleaner[0] -= 1
        else:
            if room[cleaner[0]][cleaner[1] - 1] == 0:
                cleaner[1] -= 1
    else:
        if d == 0:
            if room[cleaner[0] + 1]
        else:
            break

print(time)