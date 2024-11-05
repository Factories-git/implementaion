time = 0
say = []
plus = 1
now = True

for i in range(int(input())):
    act = 'NO'
    time = (time - 1 if time > 1 else 12) if not now else time % 12 + 1
    clock,num = input().split()
    if clock == 'HOURGLASS' and int(num) != time:
        now = not now

        print(time, act)
        continue
    if int(num) == time and clock != 'HOURGLASS':
        act = 'YES'
    print(time, act)


