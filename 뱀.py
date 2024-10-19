from collections import deque


def isgameover_wall():
    if snake[0][1] >= n or snake[0][0] >= n or snake[0][1] < 0 or snake[0][0] < 0:
        return True


def isgameover_snake():
    if snake.count(snake[0]) >= 2:
        return True


def change_direction(c):
    global now_dir
    if c == 'L':
        if now_dir == 1:
            now_dir = 2
        elif now_dir == 2:
            now_dir = -1
        elif now_dir == -1:
            now_dir = -2
        elif now_dir == -2:
            now_dir = 1
    else:
        if now_dir == 1:
            now_dir = -2
        elif now_dir == -2:
            now_dir = -1
        elif now_dir == -1:
            now_dir = 2
        else:
            now_dir = 1


direction = [0] * 10000
n = int(input())
board = [[0] * n for i in range(n)]
k = int(input())

for i in range(k):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

snake = deque([[0, 0]])

time = 1

l = int(input())
for i in range(l):
    x, c = map(str, input().split())
    direction[int(x) - 1] = c

now_dir = 1
while True:
    if now_dir == 1:
        snake.appendleft([snake[0][0], snake[0][1] + 1])
    elif now_dir == 2:
        snake.appendleft([snake[0][0] - 1, snake[0][1]])
    elif now_dir == -1:
        snake.appendleft([snake[0][0], snake[0][1] - 1])
    elif now_dir == -2:
        snake.appendleft([snake[0][0] + 1, snake[0][1]])
    if isgameover_wall():
        break
    if isgameover_snake():
        break
    if board[snake[0][0]][snake[0][1]] != 1:
        snake.pop()
    else:
        board[snake[0][0]][snake[0][1]] = 0

    if direction[time - 1] != 0:
        change_direction(direction[time - 1])

    time += 1

print(time)
