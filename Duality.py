import sys

input = sys.stdin.readline
S = -1
for i in range(int(input())):
    dot = list()
    for j in range(int(input())):
        dot.append(list(map(int, input().split())))
    dot_x = [i[0] for i in dot]
    dot_y = [i[1] for i in dot]
    for k in range(len(dot)):
        nxt = (k + 1 + 10**8) * -S
        print(k+1, dot[k][0] + nxt, dot[k][1] + nxt)
        S = -S